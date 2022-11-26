# TSC Board : industrial Raspberry Pi CM4 Carrier board

<img src="https://github.com/dumtux/tsc-controller/blob/develop/doc/image/preview.png?raw=true" style="width: 70%;">

* Raspberry Pi CM4
* HDMI 4k
* 6 x USB 2.0 Host
* 6 x isolated UART with PL2303
* 6 x Relay outputs and 4 x Digital inputs with MCP23017 I2C I/O expander
* 7 x analog inputs with MCP3008 10bit SPI ADC
* 8 x PWM outputs with PCA9685 I2C PWM controller
* RTC and EEPROM on I2C
* 2 x external I2C for external sensors
* 9 - 24V power supply input


## Issues of Ver 1.0

(todo)


## Issues of Ver 0.99

(checked item == fixed in next version)

* [x] D3, an ESD proteciton diode for USB port has wrong direction
* [x] MCP3008 is making the Raspberry CM4 not booting.
