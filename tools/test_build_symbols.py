import csv, subprocess, sys
from pathlib import Path
from kiutils.symbol import SymbolLib

REPO = Path(__file__).resolve().parents[1]
CSV = REPO / "Components" / "parts" / "dtu-shop-parts.csv"
OUT = REPO / "Components" / "symbols" / "dtu-ballerup-componentshop.kicad_sym"

def _names(sym):
    # symbol name irrespective of kiutils version (libId or entryName)
    return getattr(sym, "entryName", None) or getattr(sym, "libId", None)

def _prop(sym, key):
    for p in sym.properties:
        if p.key == key:
            return p.value
    return None

def test_build_produces_all_parts():
    subprocess.run([sys.executable, str(REPO / "tools" / "build_symbols.py")], check=True)
    lib = SymbolLib.from_file(str(OUT))
    present = {_names(s) for s in lib.symbols}
    want = {r["part"] for r in csv.DictReader(open(CSV, encoding="utf-8"))}
    missing = want - present
    assert not missing, f"missing parts: {missing}"

def test_each_part_has_footprint_and_shop_location():
    lib = SymbolLib.from_file(str(OUT))
    by_name = {_names(s): s for s in lib.symbols}
    for r in csv.DictReader(open(CSV, encoding="utf-8")):
        s = by_name[r["part"]]
        assert _prop(s, "Footprint") == r["footprint"], r["part"]
        assert _prop(s, "Shop_Location") == r["shop_location"], r["part"]

def test_roundtrip_parses():
    # re-parse must not raise
    SymbolLib.from_file(str(OUT))
