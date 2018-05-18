import vlc
import time
import _thread

def playmp3(file):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(file)
    player.set_media(media)
    player.play()
    time.sleep(1000)
    return

def play(file):
    _thread.start_new_thread(playmp3, (file, ))
    time.sleep(10000)
