import speech_recognition as sr
import relay as rl
import time
import pompatarele as ml
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print(r.recognize_google(audio))
        if(r.recognize_google(audio)=="make me coffee"):
            rl.rele1_on(21)
            time.sleep(10)#ne znaem vremeto
            rl.rele1_off()
            ml.rele2_on(20)
            time.sleep(5)
            ml.rele2_off()

