import gpiozero import LightSensor, Buzzer

ldr = LightSensor(4) #alternativka
while True
    print(ldr.value)