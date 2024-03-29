import requests
astroresponse = requests.get("http://api.open-notify.org/astros.json")
astrodata = astroresponse.json()
number = astrodata['number']
print("Number of people in space = "+str(number))
for x in range(0, number):
    name = astrodata['people'][x]['name']
    print(name)
    spacecraft = astrodata['people'][x]['craft']
    print(spacecraft)

    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    astronaut= name+"Astronaut"
    querystring = {"q":"{Astronaut}".format(Astronaut=str(astronaut)),"count":"1"}

    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    thumbnail= data['value'][0]['thumbnailUrl'] 
    print(thumbnail)
    print('')