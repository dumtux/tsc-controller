import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, address=0x20)  # MCP23017 w/ A0 set
pin0 = mcp.get_pin(0)
# pin1 = mcp.get_pin(1)
pin0.switch_to_output(value=True)
# pin1.direction = digitalio.Direction.INPUT
# pin1.pull = digitalio.Pull.UP

while True:
    pin0.value = True
    time.sleep(0.5)
    pin0.value = False
    time.sleep(0.5)
    # print("Pin 1 is at a high level: {0}".format(pin1.value))
