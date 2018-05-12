from TTS import TTS
from Recording import start_recording
from Azure_STT import azure
from Understand import luis
import json
import Functions
import _thread
import threading

def startall():
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
            Functions.start_function(intent, entities)

startall()
