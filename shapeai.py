import requests
#import os
from datetime import datetime

api_key = ' {your api id}'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

with open("output.txt","w") as file:
    file.write("Weather Stats for - {}  || {}".format(location.upper(), date_time)+
                   "Current temperature is: {:.2f} deg C".format(temp_city)+"\n"+
                   "Current weather desc  :{}".format(weather_desc)+"\n"+
                   "Current Humidity      :{}".format(hmdt)+'%'+"\n"+
                   "Current wind speed    :{}".format(wind_spd)+'kmph'
                   )



print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
