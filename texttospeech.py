from gtts import gTTS
import os
import pygame

def txt(txtu):
    z = txtu
    tts = gTTS(z, lang='en', tld='us')
    tts.save("time.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("time.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue
    
    pygame.mixer.quit()
    
    os.remove('time.mp3')

# Example usage
#text_to_speech = "Hello, this is a test."
#txt(text_to_speech)
