import speech_recognition as sr #importvame googleskata biblioteka
import relay as rl #importvame koda za nagrevatelq
import time
import pompatarele as ml #importvame koda za pompata
from gpiozero import LightSensor, Buzzer #a tuk importvame scripta koito ni raboti s fotorezistora
r = sr.Recognizer()
ldr = LightSensor(4)
rl.rele1_off()
ml.rele2_off()
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
                while ldr.value < 1: #vinagi e po malko ot 1 toest vinagi proverqva dali sveti lampata
                    if (ldr.value >0.80): #ako se e nagrqla chisloto e stoinostta na fotorezistora
                        ml.rele2_on() #puskame pompata
                        time.sleep(10) #deset sekundi kysoto kafe?!
                        ml.rele2_off() #spirame pompata da ne se oleesh
            else:
                print("Unknow Command") #ako neshto zburkash nali si ebe maikata :)
        except:
            print("Unknow Command") #tva ne znam zashto e
