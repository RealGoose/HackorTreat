import http.client
import mimetypes
import json
from hospital import getHospList
import requests
from requests import get

# Hey Franz, all of this might be a bit confusing pls ask me if u need help

def mainStructure():
    # Python Program to Get IP Address

    #Users ip address:
    ip = get('https://api.ipify.org').text
    print('Your public IP address is: {}\n'.format(ip))

    #Latitude and Longtitude of the User's IP address:
    url = "http://ip-api.com/json/"+ ip + "?fields=lat,lon"
    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    printable_response = str(response).strip("\'b")
    #print(response.text.encode('utf8'))
    #print('\n')


    #Actual Radar query:
    conn = http.client.HTTPSConnection("api.radar.io")
    payload = ''
    headers = {
      'Authorization': 'prj_test_sk_9a8f0000f39d8e0eae541935779588195a7d3401',
      #Don't steal my damn cookies
      'Cookie': '__cfduid=d6dc9a3eeb82f6b63f9ab8bbe607cfa891601077693'
    }
    #Fancy request:
    conn.request("GET", "/v1/geocode/ip?" + str(ip), payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_data = json.loads(data)

    print('1',json_data["address"]["latitude"])
    print('2',json_data["address"]["longitude"])

    #FUCK this is hard, ignore all of the stuff below I will walk u through it during the call

    #short_address = getAddressList(json_data["address"]["latitude"], json_data["address"]["longitude"])
    #shortAddressIWillUseInTheUI =[]
    #print('\n')
    
    #This shit will return addresses once I write another method,
    #If u got questions pls feel free to ask
   # for i in range(5):
    #    a = str(short_address[i]).find(",")
    #    shortAddressIWillUseInTheUI.append(short_address[i][0:a])
    #print('start:', shortAddressIWillUseInTheUI)
    #return shortAddressIWillUseInTheUI

mainStructure()
