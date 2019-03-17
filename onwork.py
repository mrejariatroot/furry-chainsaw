import speech_recognition as sr
import relay as rl
import time
import pompatarele as ml
from gpiozero import LightSensor, Buzzer
r = sr.Recognizer()
ldr = LightSensor(4)
rl.rele1_off()
ml.rele2_on()
with sr.Microphone() as source:
    while True:
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if("coffee" in text):
                print("ok")
                rl.rele1_on()
                print(ldr.value)
                while ldr.value < 0.89: #ne znaem vremeto
                    if (ldr.value >0.89):
                        ml.rele2_on()
                        ml.rele2_off()
                        time.sleep(10)
                        ml.rele2_on()
            else:
                print("Unknow Command")
        except:
            print("Unknow Command")
