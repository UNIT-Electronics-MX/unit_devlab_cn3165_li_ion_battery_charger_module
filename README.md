# CN3165 Battery Charger Module

This compact printed circuit board is designed to serve as a single-cell Li-Ion battery charger and power-out module. Its USB-C interface provides 5 V from any compliant source, powering an on-board charger IC that supports charging currents of 250 mA, 750 mA, or 1 A. Two sets of screw-terminal outputs are available:

* **Battery In:** for charging the battery safely.
* **Battery Out:** for delivering battery voltage to a load even while the battery is charging.

<div align="center">
<a href="./cn3165_battery_charger_module.pdf"><img src="hardware/resources/top.png" width="500px"><br/> UNIT charger module</a>
</div>

## Description 

### USB Power Input

The USB-C port accepts a 5 V supply from PCs, charger bricks, or power banks.

### Safety Features

Integrated safety measures include over-voltage, over-current, and thermal shutdown protections. Additionally, a reverse-current diode prevents the battery from discharging back into the USB source when disconnected or inactive.


# Pinout
<div align="center">
    <a href="#"><img src="hardware/resources/charger_pinout.jpg" width="500px"><br/>Pinout</a>
    <br/>


</div>

<div align="center">

| Component         | PCB Label   | Description                                        |
|-------------------|-------------|----------------------------------------------------|
| USB-C Connector   | USB IN      | 5 V power input from USB-C source                  |
| Connector         | Battery IN  | Screw terminals for connecting the Li-ion cell     |
| Connector         | Battery Out | Screw terminals for outputting battery voltage     |
| CHRG LED          | CHRG        | Indicator LED: on during the charging phase        |
| DONE LED          | DONE        | Indicator LED: on when the charging cycle completes|

</div>


# License MIT 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Resources

- [schematic](./hardware/UE0089-SCH-CN3165_Cargador_de_baterias-001-T.pdf)
- [Product brief](./cn3165_battery_charger_module.pdf)
