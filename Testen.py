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
        

led_1 = Led(10)
led_2 = Led(20)
led_3 = Led(30)
led_4 = Led(40)

while True:
    print("Even on, Odd off")
    GPIO.output(led_1 ,GPIO.HIGH)
    GPIO.output(led_2 ,GPIO.LOW)
    GPIO.output(led_3 ,GPIO.HIGH)
    GPIO.output(led_4 ,GPIO.LOW)

    time.sleep(1)

    print("Even off, Odd on")
    GPIO.output(led_1 ,GPIO.LOW)
    GPIO.output(led_2 ,GPIO.HIGH)
    GPIO.output(led_3 ,GPIO.LOW)
    GPIO.output(led_4 ,GPIO.HIGH)

    time.sleep(1)
