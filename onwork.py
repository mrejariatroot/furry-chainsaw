import speech_recognition as sr
import relay as rl
import time
import pompatarele as ml
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = 'vfgg' #r.recognize_google(audio)
            print(text)
            if("coffee" in text or int(input()) == 5):
                print("ok")
                rl.rele1_off()
                time.sleep(10)#ne znaem vremeto
                rl.rele1_on()
                ml.rele2_on()
                time.sleep(5)
                ml.rele2_off()
            else:
                print("Unknow Command")
        except:
            print("Unknow Command")
