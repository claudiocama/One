from playmp3 import playmp3
import datetime, time
import _thread
from TTS import TTS
import os
import urllib.request, json
import threading


#2 stringhe
def start_function(intent, entities, music):
    if intent == "Sveglia":
        alarm_clock(entities)
        return
    if intent == "Orario":
        #_thread.start_new_thread(orario, ())
        orario()
        return
    if intent == "Riproduci":
        #music = threading.Thread(target=riproduci, args=(entities[0]["entity"],))
        #music.target=riproduci
        #music.args=(entities[0]["entity"])
        #music.start()
        riproduci(entities[0]["entity"])
        return
    if intent == "Temperatura_gradi":
        temperatura_gradi()
        return

def alarm_clock(entities):
    time = datetime.datetime.now()
    numeri = []
    orari = []
    Tempo_timer = []
    timer_orari = []
    #if target_time
    dict = {"uno" : 1,"una" : 1, "zero" : 0}
    for entity in entities:
        if entity["type"] == "Numeri":
            numeri.append(entity["entity"])
        if entity["type"] == "Orari":
            orari.append(entity["entity"])
        if entity["type"] == "Tempo_timer":
            Tempo_timer.append(entity["entity"])
        if entity["type"] == "Timer_orari":
            timer_orari.append(entity["entity"])
    i=0
    for num in numeri:
        if num in dict:
            numeri[i] = dict[num]
            i+=1
    if len(numeri) == 1: #numeri
        if time.hour < int(numeri[0]):
            target_time = time
            target_time = target_time.replace(hour=int(numeri[0]), minute=0, second=0)
        else:
            target_time = time + datetime.timedelta(days=1)
            target_time = target_time.replace(hour=int(numeri[0]), minute=0, second=0)
    if len(numeri) == 2: #numeri e numeri
        if (time.hour < int(numeri[0])) or (time.hour == int(numeri[0]) and time.minute < int(numeri[1])):
            target_time = time
            target_time = target_time.replace(hour=int(numeri[0]), minute=int(numeri[1]), second=0)
        else:
            target_time = time + datetime.timedelta(days=1)
            target_time = target_time.replace(hour=int(numeri[0]), minute=int(numeri[1]), second=0)
    if len(Tempo_timer) > 0: #tempo_timer
        Tempo_timer[0] = Tempo_timer[0].split(" ")
        target_time = time
        save_pos = []
        i=0
        for x in Tempo_timer[0]:
            try:
                int(x)
                save_pos.append(i)
            except:
                pass
            i+=1
        for x in save_pos:
            1-4
            if x != len(Tempo_timer[0])-1:
                if Tempo_timer[0][x+1] == "giorno" or Tempo_timer[0][x+1] == "giorni":
                    target_time = target_time + datetime.timedelta(days=int(Tempo_timer[0][x]))
                if Tempo_timer[0][x+1] == "ora" or Tempo_timer[0][x+1] == "ore":
                    target_time = target_time + datetime.timedelta(hours=int(Tempo_timer[0][x]))
                if Tempo_timer[0][x+1] == "minuto" or Tempo_timer[0][x+1] == "minuti":
                    target_time = target_time + datetime.timedelta(minutes=int(Tempo_timer[0][x]))
                if Tempo_timer[0][x+1] == "secondo" or Tempo_timer[0][x+1] == "secondi":
                    target_time = target_time + datetime.timedelta(seconds=int(Tempo_timer[0][x]))
            else:
                target_time = target_time + datetime.timedelta(minutes=int(Tempo_timer[0][x]))

    print("sveglia impostata per le ", target_time)
    TTS("Sveglia impostata per le " + str(target_time.hour) + " e " + str(target_time.minute))
    alarm(target_time)



def alarm(target_time):
    while True:
        if target_time < datetime.datetime.now():
            playmp3("alarm1.mp3")
            break
        time.sleep(5)

def orario():
    TTS("Sono le " + str(datetime.datetime.now().hour) + " e " + str(datetime.datetime.now().minute))


    #entità: Numeri(dieci, 6), Orari(e un quarto, e mezza), Tempo_timer(tra 2 ore e 20, tra 5 minuti), Timer_orari(tra un quarto d'ora, tra mezz'ora)
    #numeri
    #numeri-numeri
    #numeri-orari
    #tempo_timer
    #tempo_timer-orari
    #timer_orari
def riproduci(canzone):
    canzone = canzone.lower()
    path = os.getcwd() + "/Music/"
    for song in os.listdir(path):
        song_l = song.lower()
        if canzone in song_l:
            playmp3("Music/"+song)

def temperatura_gradi():
    url = "http://api.openweathermap.org/data/2.5/weather?id=6537344&mode=json&units=metric&APPID=a5ae713dde9cad9023c6a8b27f015d6e"
    response = urllib.request.urlopen(url)
    output = response.read().decode('utf-8')
    my_json = json.loads(output)
    data = {"temp" : int(my_json.get('main').get('temp')), "humidity" : my_json.get('main').get('humidity'), "sunrise" : datetime.datetime.fromtimestamp(int(my_json.get('sys').get('sunrise'))).strftime('%I:%M %p'), "sunset" : datetime.datetime.fromtimestamp(int(my_json.get('sys').get('sunset'))).strftime('%I:%M %p')}
    TTS("Ci sono " + str(data["temp"]) + " gradi e c'è una percentuale di umidità del " + str(data["humidity"]) + " percento")
