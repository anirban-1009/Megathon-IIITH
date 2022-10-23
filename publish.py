import json
import time
from datetime import datetime
import paho.mqtt.client as paho  		    #mqtt library
import os
from bs4 import BeautifulSoup
import requests
from Weather import find_weather


ACCESS_TOKEN=os.environ["ACCESS_TOKEN"] #Token of your device
broker="demo.thingsboard.io"            #host name
port=1883                               #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client= paho.Client("control1")                    #create client object
client.on_publish = on_publish                     #assign function to callback
client.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard deviceclient.connect(broker,port,keepalive=60)           #establish connection


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


#the forecast part
# data = [[28, 16], [28, 99], [28, 30], [28, 14], [28, 31]]
# day = 1
# for temp,cloud in data:
#     payload="{"
#     payload+=f"\"Temperature\":{temp},"; 
#     payload+="}"
#     ret= client.publish("v1/devices/me/telemetry",payload)
#     day+=1


while True:

    res = find_weather("Hyderabad weather")
    location = res["location"]
    temp = res["temperature"]
    info = res["info"]
    payload="{"
    payload+=f"\"Temperature\":{temp},"; 
    payload+=f"\"Loc\":Hyd,";
    payload+=f"\"Info\":{info}"; 
    payload+="}"
    ret= client.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print(payload)
    time.sleep(5)