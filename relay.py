import RPi.GPIO as GPIO
import time

channel = 16

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def rele1_off():
    GPIO.output(16, GPIO.HIGH)  # Turn motor on


def rele1_on():
    GPIO.output(16, GPIO.LOW)  # Turn motor off


#if __name__ == '__main__':
#    try:
#        rele1_on(channel)
#        time.sleep(1)
#        rele1_off(channel)
#        time.sleep(1)
#        GPIO.cleanup()
#    except KeyboardInterrupt:
#        GPIO.cleanup()
