import urllib.request, config


def luis(comando):
    my_json = ""
    print(comando)
    #####TO FIX#####
    del0 = {"01" : "1", "02" : "2", "03" : "3", "04" : "4", "05" : "5", "06" : "6", "07" : "7", "08" : "8", "09" : "9"}
    for x in del0:
        if x in comando:
            comando = comando.replace(x, del0[x])
    ###############
    comando = comando.replace(" ", "%20")
    comando = comando.replace(".", "")
    try:
        response = urllib.request.urlopen("https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/6ca241bf-cf28-44d8-9c13-d8e1eb1beabb?subscription-key="+config.config("API_LUIS")+"&verbose=true&timezoneOffset=0&q="+comando)
        data = response.read()
        my_json = data.decode('utf8')
    except Exception as e:
        print(e.args)
    return my_json
