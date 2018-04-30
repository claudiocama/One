import urllib.request, json
def locate():
    response = urllib.request.urlopen("http://ipinfo.io/json")
    data = json.load(response)
    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    print(IP,org,city,country,region)
locate()
