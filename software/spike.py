import time
import board
import busio
import digitalio

from adafruit_mcp230xx.mcp23017 import MCP23017
from adafruit_pca9685 import PCA9685


i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)
pca = PCA9685(i2c)

pca.frequency = 60
pca.channels[0].duty_cycle = 0x7FFF  # output duty cycle 50%

relay6 = mcp.get_pin(13)  # Port B 5
relay6.switch_to_output(value=True)
relay6.direction = digitalio.Direction.OUTPUT

while True:
    relay6.value = True
    time.sleep(1)
    relay6.value = False
    time.sleep(1)
