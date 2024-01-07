import os
import time
import datetime



def temperature_of_raspberry_pi():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")


while True:
    with open('pi_temp.txt', 'a') as datafile:
        datafile.write(' Time: ' + str(datetime.datetime.now()))
        datafile.write(' Temp:  ' + temperature_of_raspberry_pi())
    time.sleep(2)


