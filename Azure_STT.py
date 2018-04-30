import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json, os

def azure():
    with open("temp.wav", 'rb') as fd:
        contents = fd.read()

    uri = "/speech/recognition/interactive/cognitiveservices/v1?language=it-IT&format=simple"
    headers = {'Content-Type': 'audio/wav; codec=audio/pcm; samplerate=16000', 'Ocp-Apim-Subscription-Key': "6d99488177b04ee59344c362c469a05d"}
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
    except Exception as e:
        print(e.args)
    return my_json
