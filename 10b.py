import json
cities=["banglore","udupi","karkala"]
with open ('10b.json','r') as f:
    data = json.load(f)
    city = input("Enter the city name  : ")
    if city not in cities :
        print("City not found")
    else : 
        temp = data[city]['temp']
        disc = data[city]['disc']
        hum = data[city]['humidity']
        print(temp)
        print(disc)
        print(hum)