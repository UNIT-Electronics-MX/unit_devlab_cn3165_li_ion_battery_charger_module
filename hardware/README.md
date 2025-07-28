# Hardware

<div align="center">

<a href="unit_sch_v_0_0_1_ue0089_cn3165_battery_charger.pdf"><img src="resources/img/Schematics_icon.jpg" width="300px"><br/> Schematics</a>

</div>

# Pinout

<div align="center">

<a href="#"><img src="resources/unit_pinout_v_0_0_1_ue0089_battery_charger_en.jpg" width="500px"><br/> Pinout</a>

</div>

| Component         | PCB Label   | Description                                         |
|-------------------|-----------  |---------------------------------------------------  |
| USB-C Connector   | USB IN      | 5 V power input from USB-C source                   |
| Connector         | Battery IN  | Screw terminals for connecting the Li-ion cell      |
| Connector         | Battery Out | Screw terminals for outputting battery voltage      |
| CHRG LED          | CHRG        | Indicator LED: on during the charging phase         |
| DONE LED          | DONE        | Indicator LED: on when the charging cycle completes |

# Board Dimensions

<a href="#"><img src="resources/unit_dimensions_v_0_0_1_ue0089_cn3165_battery_charger.png" width="500px"><br/> Dimensions</a>

# Board Topology

<a href="#"><img src="resources/unit_topology_v_0_0_1_ue0089_cn3165_battery_charger.png" width="500px"><br/> Topology</a>

| Ref.  | Description                                                                 |
|-------|-----------------------------------------------------------------------------|
| IC1   | CN3165 Battery Charger IC                                                   |
| L1    | Charging LED                                                                |
| L2    | Charge Done LED                                                             |
| J1    | USB Type-C Connector                                                        |
| J2    | JST PH2.0 Connector for Battery Voltage Output                              |
| J3    | JST PH2.0 Connector for Battery Input                                       |
| SB1   | 200 mA Charging Current Solder Bridge                                       |
| SB2   | 700 mA Charging Current Solder Bridge                                       |
| SP1   | Solder Pads for Battery Output                                              |
| TP1   | Battery V- Test Point                                                       |
| TP2   | Battery V+ Test Point                                                       |
| TP3   | Charging LED Test Point                                                     |
| TP4   | Charge Done LED Test Point                                                  |