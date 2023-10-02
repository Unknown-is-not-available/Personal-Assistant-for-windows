import datetime
from gtts import gTTS
import pygame
import os

d = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

def monthfind(c):
    return d[c]

def times(cmd):
    x = cmd
    time = datetime.datetime.now()
    if x == "today":
        spec = str(time.day)
        print(spec)
    elif x == "this month":
        spec = str(monthfind(time.month))
        print(spec)
    elif x == "date":
        spec = str(time.day) + monthfind(time.month)
        print(spec)
    elif x == "time":
        spec = str(time.hour) + " hours " + str(time.minute) + " minutes"
        print(spec)
    
    tts = gTTS(spec, lang='en', tld='us')
    tts.save("time.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("time.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue
    
    pygame.mixer.quit()
    
    os.remove('time.mp3')

# Example usage
#text_to_speech = "time"
#times(text_to_speech)
