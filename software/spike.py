import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, address=0x20)

relay6 = mcp.get_pin(13)  # Port B 5
relay7 = mcp.get_pin(14)  # Port B 6
relay6.switch_to_output(value=True)
relay7.switch_to_output(value=True)
relay6.direction = digitalio.Direction.OUTPUT
relay7.direction = digitalio.Direction.OUTPUT

while True:
    relay6.value = True
    time.sleep(1)
    relay6.value = False
    time.sleep(1)
    relay7.value = True
    time.sleep(1)
    relay7.value = False
    time.sleep(1)
