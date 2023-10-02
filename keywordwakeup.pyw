import speech_recognition as sr
import time
import Mainmod
from threading import Thread


#recording.adjust_for_ambient_noise(source)
def wakeupcall():
    recording = sr.Recognizer()
    with sr.Microphone() as source:
        print('Zzz...')
        audio= recording.listen(source,None,1.8)
    try:
        #output=recording.recognize_google(audio, language ="ta-IN")
        output1=recording.recognize_google(audio)
        #print('you said: '+ output )
        #print('you said: '+ output1)
        keyword=output1.lower()
        while keyword!="wake up":
            time.sleep(0.5)
            wakeupcall()
        else:
            Mainmod.mainmodule()
#            print('yes i heard ya')
    except Exception as e:
        print(e)
        wakeupcall()
        
#    t = Thread(target=wakeupcall)
#    t.start()
