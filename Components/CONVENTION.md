# Component conventions

The curated `dtu-ballerup-componentshop` symbol library contains the **named parts**
(ICs, transistors, optocouplers, specific diodes) the DTU Ballerup shop stocks, each with a
verified footprint, datasheet, and `Shop_Location` field.

**Passives are not individual symbols.** The shop stocks the full E96 resistor decade plus
common capacitor/inductor values (see `parts/dtu_component_shop.csv` for the complete list).
Use the standard KiCad generic symbols and set the value:

| Type | Symbol | Default THT footprint we stock |
|---|---|---|
| Resistor (1/4 W) | `Device:R` | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| Ceramic cap | `Device:C` | `Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm` |
| Electrolytic cap | `Device:C_Polarized` | `Capacitor_THT:CP_Radial_D8.0mm_P3.50mm` (larger for >100µF) |
| Inductor | `Device:L` | per part — most power inductors are hand-wound toroids |

`parts/dtu_component_shop.csv` is the authoritative stock inventory
(Category, Subcategory, Part_Number, Value, Description).
