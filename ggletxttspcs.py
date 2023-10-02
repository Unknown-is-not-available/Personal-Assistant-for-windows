from gtts import gTTS
import playsound
import os
spec="gotta go"
tts=gTTS(spec,lang='ta',tld='co.in')
tts.save("audio.mp3")
playsound.playsound("audio.mp3")
os.remove('audio.mp3')
