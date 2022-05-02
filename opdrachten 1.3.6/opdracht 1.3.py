import RPi.GPIO as GPIO # Only works on Raspberry Pi
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin,GPIO.LOW)
        

led_1 = Led(16)
led_2 = Led(18)
led_3 = Led(13)
led_4 = Led(15)

while True:
    print("Even on, Odd off")
    led_1.on()
    led_2.on()
    led_3.off()
    led_4.off()

    time.sleep(1)

    print("Even off, Odd on")
    led_1.off()
    led_2.off()
    led_3.on()
    led_4.on()

    time.sleep(1)
