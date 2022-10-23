import requests
import os


def getForecast(x,y):
    url = "https://api.tomorrow.io/v4/timelines"

    querystring = {
    "location":str(x) + "," + str(y),
    "fields":["temperature", "cloudCover"],
    "units":"metric",
    "timesteps":"1d",
    "apikey":os.environ["API_KEY"]}
    response = requests.request("GET", url, params=querystring)
    # print(response.text)


    results = response.json()['data']['timelines'][0]['intervals']
    res = []
    i = 1
    for daily_result in results:
        temp = round(daily_result['values']['temperature'])
        cloud = round(daily_result['values']['cloudCover'])
        res.append([temp,cloud])
        i+=1
    
    return res


def check_day(day):
    day0 = response.json()['data']['timelines'][0]['intervals']
    day0 = day[0]['startTime']
    return day0

x, y = 17.432788, 78.468997
print(getForecast(x, y)[:5])
