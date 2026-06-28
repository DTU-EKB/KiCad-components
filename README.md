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

## Table of components in EKB

|**Component**  | **Type** | **Location** | **Datasheet** | **KiCad footprint** |
|---------------|----------|--------------|---------------|---------------------|
| ESP32-wroom32 | SMD MCU  | EKBB         | [Datasheet (external)](https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html) | |

## Location abbreviation:
- CSM:  DTU Ballerup Components shop main storage.
- CSB:  DTU Ballerup Components shop back room storage. You need to specifically ask a professor for this part.
- EKBM: EKB main storage: Can be found in komponents shelves in EKB. ***Membership needed***.
- EKBB: EKB Basement/Backup storage: These components can be given upon request, if still in stock. ***Membership needed***.
