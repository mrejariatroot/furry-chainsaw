import speech_recognition as sr
import relay as rl

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print(r.recognize_google(audio))
    if(r.recognize_google(audio)=="make me coffee"):
        rl.motor_on(21)
        rl.motor_off(21)
        
        


