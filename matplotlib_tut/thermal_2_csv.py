import csv
import time
import busio
import board
import adafruit_amg88xx
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

while True:
    
    for row in amg.pixels:
        # Pad to 1 decimal place
        print(["{0:.1f}".format(temp) for temp in row])
		rows = float(["{0:.1f}".format(temp)])
		fliename = "test.csv"
		print("")
		
		with open(filename, 'w') as csvfile
			# creating a csv writer object 
			csvwriter = csv.writer(csvfile) 
			        
			# writing the data rows 
			csvwriter.writerows(rows)
    print("\n")
    time.sleep(1)

		
