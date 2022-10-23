# import python_weather
# import asyncio
# import os

# city = "Hyderabad"

# async def getweather(city):
#   # declare the client. format defaults to the metric system (celcius, km/h, etc.)
#   async with python_weather.Client(format=python_weather.METRIC) as client:

#     # fetch a weather forecast from a city
    
#     weather = await client.get(city)
  
#     # returns the current day's forecast temperature (int)
#     res = round(weather.current.temperature, 2)
#     return res
  
#     # get the weather forecast for a few days
#     # for forecast in weather.forecasts:
#     #   print(forecast.date, forecast.astronomy) 
  
#     #   # hourly forecasts
#     #   for hourly in forecast.hourly:
#     #     print(f' --> {hourly!r}')

# if __name__ == "__main__":
#   # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
#   # for more details
#   if os.name == "nt":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#   print(asyncio.run(getweather(city)))

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def find_weather(city_name):
   city_name = city_name.replace(" ", "+")
 
   try:
       res = requests.get(
           f'https://www.google.com/search?q={city_name}&oq={city_name}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
      
       print("Loading...")
 
       soup = BeautifulSoup(res.text, 'html.parser')
       location = soup.select('#wob_loc')[0].getText().strip()
       info = soup.select('#wob_dc')[0].getText().strip()
       temperature = soup.select('#wob_tm')[0].getText().strip()

       res = {"location":location,"temperature":temperature,"info":info}
 
       return res
   except:
       print("Please enter a valid city name")

if __name__ == "__main__":
    print(find_weather("Hyderabad weather"))