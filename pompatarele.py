import RPi.GPIO as GPIO
import time

channel = 20

# GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  #vkliuchvane na pompata


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW) #izkliuchvane na pompata


if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
        motor_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
