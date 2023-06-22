import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)
pwm=GPIO.PWM(40,50)
pwm.start(0)

try:
    while True:
        DC=[2,5,12]
        for i in (DC):
            pwm.ChangeDutyCycle(i)
            print(i)
            sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
