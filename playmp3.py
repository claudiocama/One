import vlc
import time

def playmp3(file):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(file)
    player.set_media(media)
    player.play()
    time.sleep(1000)
