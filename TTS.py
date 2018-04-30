from gtts import gTTS
from playmp3 import playmp3

def TTS(stringa):
    tts = gTTS(text=stringa, lang="it")
    tts.save("TTS.mp3")
    playmp3("TTS.mp3")

