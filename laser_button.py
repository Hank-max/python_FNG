from gpiozero import Button,LED #using this button function for the laser sensor
from time import sleep
relay = LED(17)

def solid_laser():
    relay.off()
    print("Apple trees safe")

laser = Button(18, bounce_time=0.1) #i may add a pull up resistor if there is lots of noise
laser.when_pressed = solid_laser

while True:
    print("Who crossed my laser")
    relay.on()
    sleep(2)