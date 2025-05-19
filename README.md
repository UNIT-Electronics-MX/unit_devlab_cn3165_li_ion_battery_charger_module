# CN3165 Battery Charger Module

This compact printed circuit board is designed to serve as a single-cell Li-Ion battery charger and power-out module. Its USB-C interface provides 5 V from any compliant source, powering an on-board charger IC that supports charging currents of 250 mA, 750 mA, or 1 A. Two sets of screw-terminal outputs are available:

* **Battery In:** for charging the battery safely.
* **Battery Out:** for delivering battery voltage to a load even while the battery is charging.

<a href="#"><img src="hardware/resources/charger_module.jpg" width="500px"><br/> UNIT charger module</a>

## Description 

### USB Power Input

The USB-C port accepts a 5 V supply from PCs, charger bricks, or power banks.

### Safety Features

Integrated safety measures include over-voltage, over-current, and thermal shutdown protections. Additionally, a reverse-current diode prevents the battery from discharging back into the USB source when disconnected or inactive.


# Pinout

<a href="#"><img src="hardware/resources/charger_pinout.jpg" width="500px"><br/> Pinout</a>

| Component         | PCB Label   | Description                                         |
|-------------------|-----------  |---------------------------------------------------  |
| USB-C Connector   | USB IN      | 5 V power input from USB-C source                   |
| Connector         | Battery IN  | Screw terminals for connecting the Li-ion cell      |
| Connector         | Battery Out | Screw terminals for outputting battery voltage      |
| CHRG LED          | CHRG        | Indicator LED: on during the charging phase         |
| DONE LED          | DONE        | Indicator LED: on when the charging cycle completes |
