from TTS import TTS
from Recording import start_recording
from pocketsphinx import LiveSpeech
from Azure_STT import azure
from Understand import luis
import json
import Functions
import _thread
import threading
#import datetime


#for phrase in LiveSpeech():
#    name = str(phrase)
#   if name == "one" or name == "One":
def startall():
        music = threading.Thread()
        start_recording()
        comando = azure()
        print(comando)
        parsed = json.loads(comando)
        print("Response:")
        if parsed["RecognitionStatus"] == "Success":
            parsed_luis = json.loads(luis(parsed["DisplayText"]))
            print(json.dumps(parsed_luis, indent=2))
            intent = parsed_luis["topScoringIntent"]["intent"]
            entities = []
            for x in parsed_luis["entities"]:
                entities.append(x)
            #if intent == "Orario":
                #TTS("Sono le " + str(datetime.datetime.now().hour) + " e " + str(datetime.datetime.now().minute))
            Functions.start_function(intent, entities, music)
            #_thread.start_new_thread(Functions.start_function, (intent, entities,))

startall()
