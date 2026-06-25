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

|**Component** | **Type** | **Location** | **Datasheet** |
|--------------|----------|-------------------|---|
| MCP6002 | Op-Amp | CSM | [Datasheet (In repo)](https://github.com/DTU-EKB/KiCad-components/blob/main/datasheets/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf) |

### Location abbreviation:
- CSM: DTU Ballerup Components shop main storage.
- CSB: DTU Ballerup Components shop back room storage. You need to specifically ask a professor for this part.
