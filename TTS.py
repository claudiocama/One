from gtts import gTTS
from playmp3 import play
import _thread


def TTS(stringa):
    tts = gTTS(text=stringa, lang="it")
    tts.save("TTS.mp3")
    play("TTS.mp3")
