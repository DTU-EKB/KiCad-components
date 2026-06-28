#!/usr/bin/env python3
"""Generate dtu-ballerup-componentshop.kicad_sym from the curated CSV.

For each CSV row:
  - part == source_symbol  -> copy that stock symbol verbatim, then override fields ("self")
  - part != source_symbol  -> copy the base symbol once, then add a derived
                              symbol `part (extends source_symbol)` with overridden fields
Idempotent: fully regenerates the output file each run.
"""
import csv
import copy
from pathlib import Path
from kiutils.symbol import SymbolLib, Symbol
from kiutils.items.common import Property

STOCK = Path(r"C:/Program Files/KiCad/10.0/share/kicad/symbols")
REPO = Path(__file__).resolve().parents[1]
CSV = REPO / "Components" / "parts" / "dtu-shop-parts.csv"
OUT = REPO / "Components" / "symbols" / "dtu-ballerup-componentshop.kicad_sym"

_stock_cache = {}


def stock_lib(name):
    if name not in _stock_cache:
        _stock_cache[name] = SymbolLib.from_file(str(STOCK / f"{name}.kicad_sym"))
    return _stock_cache[name]


def sym_name(sym):
    return getattr(sym, "entryName", None) or getattr(sym, "libId", None)


def find(lib, name):
    for s in lib.symbols:
        if sym_name(s) == name:
            return s
    raise KeyError(f"{name} not found in {lib.filePath}")


def get_prop(sym, key):
    for p in sym.properties:
        if p.key == key:
            return p
    return None


def set_prop(sym, key, value):
    p = get_prop(sym, key)
    if p is None:
        sym.properties.append(Property(key=key, value=value))
    else:
        p.value = value


def apply_fields(sym, row):
    set_prop(sym, "Value", row["part"])
    set_prop(sym, "Footprint", row["footprint"])
    set_prop(sym, "Datasheet", row["datasheet"])
    set_prop(sym, "Description", row["description"])
    set_prop(sym, "Shop_Location", row["shop_location"])


def rename_symbol(sym, new_name):
    """Rename a concrete symbol and any child unit symbols that embed the parent name."""
    old_name = sym_name(sym)
    if hasattr(sym, "entryName"):
        sym.entryName = new_name
    if hasattr(sym, "libId"):
        sym.libId = new_name
    for u in getattr(sym, "units", []) or []:
        un = sym_name(u)
        if un and old_name and un.startswith(old_name):
            new_un = new_name + un[len(old_name):]
            if hasattr(u, "entryName"):
                u.entryName = new_un
            if hasattr(u, "libId"):
                u.libId = new_un


def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    out = SymbolLib(version="20251024", generator="dtu_build_symbols")
    # Map (source_lib, source_symbol) -> cloned Symbol object in `out`
    copied_bases = {}

    # Pass 1: copy each needed base/concrete stock symbol exactly once.
    for r in rows:
        key = (r["source_lib"], r["source_symbol"])
        if key in copied_bases:
            continue
        src = find(stock_lib(r["source_lib"]), r["source_symbol"])
        clone = copy.deepcopy(src)
        out.symbols.append(clone)
        copied_bases[key] = clone

    # Pass 2: realize each catalog part.
    for r in rows:
        base = copied_bases[(r["source_lib"], r["source_symbol"])]
        if r["part"] == r["source_symbol"]:
            # "self" case: the base symbol IS this catalog part — rename & apply fields
            rename_symbol(base, r["part"])
            apply_fields(base, r)
        else:
            # Derived case: add a new symbol that extends the base
            ref_prop = get_prop(base, "Reference")
            ref = ref_prop.value if ref_prop else "U"
            derived = Symbol(
                entryName=r["part"],
                extends=sym_name(base),
                inBom=True,
                onBoard=True,
            )
            apply_fields(derived, r)
            # Set Reference to match base
            set_prop(derived, "Reference", ref)
            out.symbols.append(derived)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_file(str(OUT))
    print(f"wrote {OUT} with {len(out.symbols)} symbols")


if __name__ == "__main__":
    main()
