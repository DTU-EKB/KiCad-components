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

> Full machine-readable inventory: [`Components/parts/dtu_component_shop.csv`](Components/parts/dtu_component_shop.csv) (1464 parts). See [`Components/CONVENTION.md`](Components/CONVENTION.md) for the passives convention.

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
| LM317T        | Adjustable regulator, TO-220 (ADJ-OUT-IN) | CSM | [Datasheet (external)](https://www.ti.com/lit/ds/symlink/lm317.pdf) | Package_TO_SOT_THT:TO-220-3_Vertical † |
| LED 3MM RØD / GUL / GRØN | 3 mm LED | CSM |          | LED_THT:LED_D3.0mm † |
| Pushbutton    | 6 mm tactile, momentary | CSM |           | Button_Switch_THT:SW_PUSH_6mm † |
| Header Male   | 2.54 mm straight pin header, break to length | CSM | | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical † (1x`NN` for other lengths) |
| 1µF, 10µF     | Electrolytic cap, small | CSM |           | Capacitor_THT:CP_Radial_D5.0mm_P2.00mm † |
| 100n          | Ceramic cap | CSM |                      | Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm † |

† Fit confirmed by assembly: these parts were soldered into these footprints on a working board ([esp32-solder-test](https://github.com/MadsRudolph/personal-projects/tree/main/esp32-solder-test), 2026-09-26). They were not caliper-measured, so add them to the table below if you measure one.

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
| ESP32-wroom32 | SMD MCU  | EKBB         | [Datasheet (external)](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html) | ekb-component-stock:ESP32-WROOM-32_NoVias ‡ |

‡ The stock `RF_Module:ESP32-WROOM-32` footprint with the twelve 0.2 mm thermal vias in the centre pad removed, for single-sided boards. It was proven on a hand-soldered, fiber-laser-etched board that ran WiFi ([esp32-solder-test](https://github.com/MadsRudolph/personal-projects/tree/main/esp32-solder-test), 2026-09-26). The centre GND pad can be left unsoldered by hand; GND reaches the module through pins 1, 15 and 38. The module's pad gaps are 0.37 mm, so it cannot be isolation-milled with a 0.8 mm end mill; etch it with the laser. The shop has no 3.3 V LDO, so power it from the `LM317T` (243R / 392R = 3.27 V). Fed from 5 V with 10 µF on 3V3, WiFi peaks reset the module; the recommended (not yet built) fix is 7-9 V in and ≥470 µF on 3V3.

## Location abbreviation:
- CSM:  DTU Ballerup Components shop main storage.
- CSB:  DTU Ballerup Components shop back room storage. You need to specifically ask a professor for this part.
- EKBM: EKB main storage: Can be found in komponents shelves in EKB. ***Membership needed***.
- EKBB: EKB Basement/Backup storage: These components can be given upon request, if still in stock. ***Membership needed***.
