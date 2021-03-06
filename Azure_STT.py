import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json, os, config

def azure():
    with open("temp.wav", 'rb') as fd:
        contents = fd.read()

    headers = {'Content-Type': 'audio/wav; codec=audio/pcm; samplerate=16000', 'Ocp-Apim-Subscription-Key': config.config("API_STT")}
    try:
        params = urllib.parse.urlencode({
        })
        body = contents
        conn = http.client.HTTPSConnection('speech.platform.bing.com')
        conn.request("POST", "/speech/recognition/interactive/cognitiveservices/v1?language=it-IT&format=simple%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        # 'data' contains the JSON data. The following formats the JSON data for display.
        my_json = data.decode('utf8')
        conn.close()
        os.remove("temp.wav")
        return my_json
    except Exception as e:
        print(e.args)
