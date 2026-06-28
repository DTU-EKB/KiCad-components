#!/usr/bin/env python3
"""Generate dtu-ballerup-componentshop.kicad_sym from the curated CSV.

Stock KiCad symbols are copied as VERBATIM TEXT blocks (not round-tripped
through a parser) so that multi-unit symbol structure is preserved exactly --
KiCad rejects libraries whose unit sub-symbol names get mangled.

For each CSV row:
  - part == source_symbol  -> copy that stock symbol verbatim, then override
                              the catalog fields in place ("self")
  - part != source_symbol  -> copy the base symbol once and add a small derived
                              symbol `part (extends source_symbol)` ("derived")

Every `extends` ancestor is copied too, because KiCad resolves inheritance only
within a single library file. Idempotent: fully regenerates the output file.
"""
import csv
import re
from pathlib import Path

STOCK = Path(r"C:/Program Files/KiCad/10.0/share/kicad/symbols")
REPO = Path(__file__).resolve().parents[1]
CSV = REPO / "Components" / "parts" / "dtu-shop-parts.csv"
OUT = REPO / "Components" / "symbols" / "dtu-ballerup-componentshop.kicad_sym"

HEADER = (
    "(kicad_symbol_lib\n"
    "\t(version 20251024)\n"
    '\t(generator "kicad_symbol_editor")\n'
    '\t(generator_version "10.0")'
)

_text_cache = {}


def stock_text(libname):
    if libname not in _text_cache:
        _text_cache[libname] = (STOCK / f"{libname}.kicad_sym").read_text(encoding="utf-8")
    return _text_cache[libname]


def esc(v):
    return v.replace("\\", "\\\\").replace('"', '\\"')


def block_end(text, open_idx):
    """Return the index just past the ')' that closes the '(' at/after open_idx,
    respecting double-quoted strings and backslash escapes."""
    depth = 0
    in_str = False
    escaped = False
    for j in range(open_idx, len(text)):
        c = text[j]
        if in_str:
            if escaped:
                escaped = False
            elif c == "\\":
                escaped = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return j + 1
    raise ValueError("unbalanced parentheses")


def extract_block(libname, name):
    """Return the verbatim top-level (symbol "name" ...) block text from a stock lib."""
    text = stock_text(libname)
    m = re.search(r'(?m)^\t\(symbol "%s"' % re.escape(name), text)
    if not m:
        raise KeyError(f"{name} not found in {libname}.kicad_sym")
    start = m.start()
    paren = text.index("(", start)
    return text[start:block_end(text, paren)]


def base_ref(blk):
    m = re.search(r'\(property "Reference" "([^"]*)"', blk)
    return m.group(1) if m else "U"


def set_prop_value(blk, key, value):
    pat = r'(\(property "%s" )"(?:\\.|[^"\\])*"' % re.escape(key)
    return re.sub(pat, lambda m: m.group(1) + '"' + esc(value) + '"', blk, count=1)


def inject_after_reference(blk, props_text):
    i = blk.index('(property "Reference"')
    end = block_end(blk, blk.index("(", i))
    return blk[:end] + "\n" + props_text.rstrip("\n") + blk[end:]


def apply_self_fields(blk, row):
    """Override the catalog fields on a verbatim 'self' symbol block."""
    fields = [
        ("Value", row["part"]),
        ("Footprint", row["footprint"]),
        ("Datasheet", row["datasheet"]),
        ("Description", row["description"]),
        ("Shop_Location", row["shop_location"]),
    ]
    inject = []
    for key, val in fields:
        if '(property "%s" "' % key in blk:
            blk = set_prop_value(blk, key, val)
        else:
            inject.append((key, val))
    if inject:
        props = "".join(
            '\t\t(property "%s" "%s" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            % (k, esc(v))
            for k, v in inject
        )
        blk = inject_after_reference(blk, props)
    return blk


def make_derived(row, base_blk):
    ref = base_ref(base_blk)
    p = lambda k, v, hide: '\t\t(property "%s" "%s" (at 0 0 0) (effects (font (size 1.27 1.27))%s))' % (
        k, esc(v), " (hide yes)" if hide else "")
    return "\n".join([
        '\t(symbol "%s"' % row["part"],
        '\t\t(extends "%s")' % row["source_symbol"],
        p("Reference", ref, False),
        p("Value", row["part"], False),
        p("Footprint", row["footprint"], True),
        p("Datasheet", row["datasheet"], True),
        p("Description", row["description"], True),
        p("Shop_Location", row["shop_location"], True),
        "\t)",
    ])


def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))

    ordered = []          # symbol names in output order
    block_by_name = {}    # name -> block text
    base_lib = {}         # base symbol name -> its source lib (for parent lookups)

    def emit_base(libname, name):
        if name in block_by_name:
            return
        blk = extract_block(libname, name)
        # Emit any extends-parent (same lib) first so ancestors precede children.
        pm = re.search(r'\(extends "([^"]+)"', blk)
        if pm:
            emit_base(libname, pm.group(1))
        block_by_name[name] = blk
        base_lib[name] = libname
        ordered.append(name)

    # Pass 1: emit every base/concrete stock symbol (and its ancestor chain).
    for r in rows:
        emit_base(r["source_lib"], r["source_symbol"])

    # Pass 2: realize each catalog part.
    for r in rows:
        if r["part"] == r["source_symbol"]:
            block_by_name[r["part"]] = apply_self_fields(block_by_name[r["part"]], r)
        else:
            block_by_name[r["part"]] = make_derived(r, block_by_name[r["source_symbol"]])
            ordered.append(r["part"])

    content = HEADER + "\n" + "\n".join(block_by_name[n] for n in ordered) + "\n)\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} with {len(ordered)} symbols")


if __name__ == "__main__":
    main()
