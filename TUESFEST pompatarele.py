import RPi.GPIO as GPIO
import time

channel = 26

# GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def rele2_off():
    GPIO.output(26, GPIO.HIGH)  #vkliuchvane na pompata


def rele2_on():
    GPIO.output(26, GPIO.LOW) #izkliuchvane na pompata


#if __name__ == '__main__':
    #try:
        #rele2_on(channel)
        #time.sleep(1)
        #rele2_off(channel)
        #time.sleep(1)
        #GPIO.cleanup()
    #except KeyboardInterrupt:
        #GPIO.cleanup()
