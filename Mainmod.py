import speech_recognition as sr
import os
import timemod
import keywordwakeup
#import boteh
import openmod
import closemod
import search
import googleserach
import movieopnmod



def mainmodule():
    try:
        recording = sr.Recognizer()
        #recording.pause_threshold=0.8
        with sr.Microphone() as source:

            print('Say Something...')
            audio= recording.listen(source,None,3)

        try:
            #output=recording.recognize_google(audio, language ="ta-IN")
            output1=recording.recognize_google(audio)
            #print('you said: '+ output )
            print('you said: '+output1)
        
            voicein=output1
            cmd=voicein.lower().split(" ",1)
        
            if cmd[0]=="time"or cmd[0]=="this month"or cmd[0]=="date"or cmd[0]=="today":
                timemod.times(cmd[0])
            elif cmd[0]=='open':
                openmod.opens(cmd[1])
            elif cmd[0]=='close':
                closemod.closes(cmd[1])
            elif cmd[0]=='search':
                search.gserch(cmd[1])
            elif cmd[0]=='google':
                googleserach.searches(cmd[1])
            elif cmd[0]=='movie':
                movieopnmod.movies(cmd[1])
            else:
                pass
                #boteh.botehh(voicein)     
                
            
            mainmodule()   
                    
        
        except Exception as e:
            print('error')
            keywordwakeup.wakeupcall()

    except Exception as e:
        print("err")
       
mainmodule()








#                                                                                                                                       Done by
#                                                                                                                                           Mr. Unknown
#                                                                                                                                           Mr. Trident Nivas


    
