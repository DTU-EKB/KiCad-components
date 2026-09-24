# KiCad-components
Repository of the electrical components DTU Ballerup and EKB has in stock

## Adding library to KiCad
To add this library to KiCad, go into *Plugin and Content Manager* on the KiCad project screen, then click *Manage* beside the Repository drop-down menu, then click the small plus icon and paste:
```bash
https://raw.githubusercontent.com/DTU-EKB/KiCad-components/main/repository.json
```
... into the field.

After this is done, reflesh the *Plugin and Content Manager* window, and you should be able to install and keep the component library up to date.

If you find missing components, footprints and datasheets, please consider contributing back to the project, and learn a bit about Git and Github in the process :)

---
## Table of components in the component shop

|**Component**  | **Type** | **Location** | **Datasheet** | **KiCad footprint** |
|---------------|----------|--------------|---------------|---------------------|
| Resistors     |          | CSM          |               | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal |
| Diodes        |          | CSM          |               | Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal |
| MCP6002       | Op-Amp   | CSM          | [Datasheet (In repo)](https://github.com/DTU-EKB/KiCad-components/blob/main/datasheets/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf) | Package_DIP:DIP-8_W7.62mm_LongPads |
| 2u2           | Film cap, 63 V  | CSM   |               | Capacitor_THT:C_Rect_L26.5mm_W7.0mm_P22.50mm_MKS4 |
| 3u3           | Film cap, 100 V | CSM   |               | Capacitor_THT:C_Rect_L26.5mm_W8.5mm_P22.50mm_MKS4 |
| 6u8           | Film cap, 100 V | CSM   |               | Capacitor_THT:C_Rect_L31.5mm_W11.0mm_P27.50mm_MKS4 |
| 8u2           | Film cap, 600 V | CSM   |               | Capacitor_THT:C_Rect_L31.5mm_W13.0mm_P27.50mm_MKS4 |
| 4R7 5W        | Power resistor, axial | CSM |           | Resistor_THT:R_Axial_Power_L25.0mm_W9.0mm_P27.94mm |
| 10R 5W        | Power resistor, axial | CSM |           | Resistor_THT:R_Axial_Power_L20.0mm_W6.4mm_P22.40mm |
| 2 pol skrueterminal | Screw terminal, 5 mm | CSM |      | TerminalBlock:TerminalBlock_MaiXu_MX126-5.0-02P_1x02_P5.00mm |

## Measured dimensions of component-shop parts

The shop lists no body sizes, so these were measured with calipers on the actual parts. All sizes in mm. Pitch is centre to centre: measure the leads outside to outside where they leave the body, then subtract one lead Ø. Add a row whenever you measure a new part, so nobody has to measure it again.

| **Component** | **Type** | **Lead pitch** | **Body L × W × H** | **Lead Ø** | **Rating** | **KiCad footprint** | **Measured** |
|---------------|----------|---------------:|--------------------|-----------:|-----------|---------------------|--------------|
| 2u2 | Film cap, radial box | 22.5 (22.6 measured) | 25.7 × 6.2 × 15 | 0.7 | 63 V | Capacitor_THT:C_Rect_L26.5mm_W7.0mm_P22.50mm_MKS4 | 2026-09-24 |
| 3u3 | Film cap, radial box | 22.5 (22.7 measured) | 25 × 8.2 × 17.8 | 0.7 | 100 V | Capacitor_THT:C_Rect_L26.5mm_W8.5mm_P22.50mm_MKS4 | 2026-09-24 |
| 6u8 | Film cap, radial box | 27.5 (27.3 measured) | 31 × 11 × 21 | 0.7 | 100 V | Capacitor_THT:C_Rect_L31.5mm_W11.0mm_P27.50mm_MKS4 | 2026-09-24 |
| 8u2 | Film cap, radial box | 27.5 (27.3 measured) | 31.5 × 13.3 × 28 | 0.7 | 600 V | Capacitor_THT:C_Rect_L31.5mm_W13.0mm_P27.50mm_MKS4 | 2026-09-24 |
| 4R7 5W | Power resistor, axial, cylindrical | 27.94 (27.8 bent) | 24 × Ø8.5 | 0.7 | 5 W | Resistor_THT:R_Axial_Power_L25.0mm_W9.0mm_P27.94mm | 2026-09-24 |
| 10R 5W | Power resistor, axial | 22.4 (21.3 bent) | 18 × 6 × 6 | 0.7 | 5 W | Resistor_THT:R_Axial_Power_L20.0mm_W6.4mm_P22.40mm | 2026-09-24 |
| 2 pol skrueterminal | Screw terminal, 2-pole | 5.0 | matches stock footprint | | | TerminalBlock:TerminalBlock_MaiXu_MX126-5.0-02P_1x02_P5.00mm | 2026-09-24 |

## Table of components in EKB

|**Component**  | **Type** | **Location** | **Datasheet** | **KiCad footprint** |
|---------------|----------|--------------|---------------|---------------------|
| ESP32-wroom32 | SMD MCU  | EKBB         | [Datasheet (external)](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html) | |

## Location abbreviation:
- CSM:  DTU Ballerup Components shop main storage.
- CSB:  DTU Ballerup Components shop back room storage. You need to specifically ask a professor for this part.
- EKBM: EKB main storage: Can be found in komponents shelves in EKB. ***Membership needed***.
- EKBB: EKB Basement/Backup storage: These components can be given upon request, if still in stock. ***Membership needed***.
