# DevLab: CN3165 Li-Ion Battery Charger Module
This compact printed circuit board is designed to serve as a single-cell Li-Ion battery charger and power-out module. Its USB-C interface provides 5 V from any compliant source, powering an on-board charger IC that supports charging currents of 250 mA, 750 mA, or 1 A*. Two sets of terminals are available:

* **Battery In:** for charging the battery safely.
* **Battery Out:** for delivering battery voltage to a load even while the battery is charging.

> **Note:** *The charging current will depend on the battery charge percentage.*

<div align="center">
<a href="./hardware/resources/unit_product_top_v_0_0_1_ue0089_cn3165_battery_charger.png"><img src="hardware/resources/unit_product_top_v_0_0_1_ue0089_cn3165_battery_charger.png" width="400px"></a>
</div>


<div align="center">

### Quick Setup


[<img src="https://img.shields.io/badge/Product%20Wiki-blue?style=for-the-badge" alt="Product Wiki">](#)
[<img src="https://img.shields.io/badge/Datasheet-green?style=for-the-badge" alt="Datasheet">](https://unit-electronics-mx.github.io/unit_devlab_cn3165_li_ion_battery_charger_module/hardware/DevLab%20CN3165%20Li-Ion%20Battery%20Charger%20Module.docx.pdf)
[<img src="https://img.shields.io/badge/Buy%20Now-orange?style=for-the-badge" alt="Buy Now">](https://uelectronics.com/)
[<img src="https://img.shields.io/badge/Getting%20Started-purple?style=for-the-badge" alt="Getting Started">](#)

</div>


## Description 

### USB Power Input

The USB-C port accepts a 5 V supply from PCs, charger bricks, or power banks.

### Safety Features

Integrated safety measures include over-voltage, over-current protection up to 5A; over-discharge, short circuit and polarity protection; and thermal shutdown.

### Output Features

Up to 3A output current from output terminals. The module can operate with currents above 3A with proper thermal management. Keep the module below 150°C to avoid permanent damage to the device.

### Current Charge Configurable

Select charging current using the designated solder bridges. The current can be configured to 250 mA, 750 mA, or 1000 mA.

# License MIT 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Resources

- [Schematic PDF](hardware/unit_sch_v_0_0_1_ue0089_cn3165_battery_charger.pdf)
- [Product brief](./cn3165_battery_charger_module.pdf)
