import time
import busio
import board
import adafruit_amg88xx
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

#this is just a git test

while True:
    
    for row in amg.pixels:
        # Pad to 1 decimal place
        print(["{0:.1f}".format(temp) for temp in row])
        print("")
    print("\n")
    time.sleep(1)
