---
title: "CN3165 battery charger module"
version: "1.0"
modified: "2025-05-02"
output: "cn3165_battery_charger_module"
subtitle: "This compact printed circuit board functions as both a single-cell Li-Ion battery charger and a power-out module"
---

<!--
# README_TEMPLATE.md
Este archivo sirve como entrada para generar un PDF técnico estilo datasheet.
Edita las secciones respetando el orden, sin eliminar los encabezados.
-->
 <!-- logo -->

# cn3165_battery_charger_module

![product](./images/product.jpg)

## Introduction

This compact printed circuit board functions as both a single-cell Li-Ion battery charger and a power-out module. It features a USB-C interface that accepts a stable 5 V supply from sources such as PCs, charger bricks, or power banks, and includes an on-board charger IC that supports charging currents of 250 mA, 750 mA, or 1 A. Additionally, two dedicated screw-terminal outputs provide a secure pathway for charging (Battery In) and deliver battery voltage to a load even during charging (Battery Out), making it suitable for portable applications that demand simultaneous charging and power delivery.

## Functional Description

- The USB-C port accepts a 5 V supply from PCs, charger bricks, or power banks.
- The CN3165 IC manages the charging process safely with automatic preconditioning, constant current, and constant voltage phases.
- CHRG and DONE LEDs indicate the charging status clearly.
- Battery Out terminals remain powered even during the charging cycle, enabling uninterrupted device usage.

## Electrical Characteristics & Signal Overview

- Input Voltage: 5 V (USB-C)
- Charging Current Options: 250 mA, 750 mA, 1 A (configurable via resistor)
- Battery Chemistry: Single-cell Li-Ion
- Charge Termination: Voltage threshold and current taper
- Status Indicators: CHRG (charging), DONE (charge complete)

## Applications

- Battery charger for single-cell Li-Ion batteries
- Power supply for low-power devices
- Educational prototyping with power delivery requirements
- Portable sensors and microcontroller systems
- USB-powered battery packs

## Features

- USB-C power input
- Selectable charging current
- Screw terminals for robust battery connections
- Independent charge and power output paths
- LED indicators for charge status
- Compact PCB footprint

## Pin & Connector Layout

| Component         | PCB Label   | Description                                         |
|-------------------|-----------  |---------------------------------------------------  |
| USB-C Connector   | USB IN      | 5 V power input from USB-C source                   |
| Connector         | Battery IN  | Screw terminals for connecting the Li-ion cell      |
| Connector         | Battery Out | Screw terminals for outputting battery voltage      |
| CHRG LED          | CHRG        | Indicator LED: on during the charging phase         |
| DONE LED          | DONE        | Indicator LED: on when the charging cycle completes |

## Settings

### Interface Overview

| Interface  | Signals / Pins            | Typical Use                                         |
|------------|----------------------------|-----------------------------------------------------|
| USB-C      | VBUS, GND                  | Power input (5 V)                                   |
| Battery IN | B+, B-                     | Connects to Li-Ion cell terminals                   |
| Battery OUT| OUT+, OUT-                 | Provides battery voltage to external load           |
| LEDs       | CHRG, DONE                 | Status indication via onboard LEDs                  |

### Supports

| Symbol | I/O   | Description                         |
| ------ | ----- | ----------------------------------- |
| CHRG   | O     | Active-low signal when charging     |
| DONE   | O     | Active-high when charging complete  |

## Block Diagram

![Function Diagram](images/function-diagram.jpg)

## Dimensions

![Dimensions](images/dimensions.png)

## Usage

Works with:

- Single-cell 3.7 V Li-Ion batteries
- USB power sources (laptops, power banks, adapters)
- Low-power microcontroller projects
- Systems requiring charge-while-operating configuration

## Downloads

- [Schematic PDF](https://github.com/UNIT-Electronics-MX/unit_cn3165_battery_charger_module/tree/main/hardware)

## Purchase

- [Buy from UNIT Electronics](https://www.uelectronics.com)
