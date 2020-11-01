import http.client
import mimetypes
import json
import requests
from GarageSaleScrapper import *
from apiCalls import getAddressList
from requests import get

def mainStructure(numSales, dateInput):
    # Python Program to Get IP Address

    #Users ip address:
    ip = get('https://api.ipify.org').text
    print('Your public IP address is: {}\n'.format(ip))

    #Latitude and Longtitude of the User's IP address:
    url = "http://ip-api.com/json/"+ ip + "?fields=lat,lon"  
    #zipCode = "http://ip-api.com/json/"+ ip + "?fields=zip"
    payload = {}
    headers= {}
    

    response = requests.request("GET", url, headers=headers, data = payload)
    printable_response = str(response).strip("\'b")
    #print('\n\n', payload)

    #Actual Radar query:
    conn = http.client.HTTPSConnection("api.radar.io")
    payload = ''
    headers = {
      'Authorization': 'prj_test_sk_9a8f0000f39d8e0eae541935779588195a7d3401',
      'Cookie': '__cfduid=d6dc9a3eeb82f6b63f9ab8bbe607cfa891601077693'
    }
    
    #Fancy request:
    conn.request("GET", "/v1/geocode/ip?" + str(ip), payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_data = json.loads(data)
    #print('latitude:',json_data["address"]["latitude"])
    #print('longitude:',json_data["address"]["longitude"])

    #getAddressList(json_data["address"]["latitude"], json_data["address"]["longitude"])
    location, short_address = WebScrapper(92620, json_data["address"]["latitude"], json_data["address"]["longitude"], numSales, dateInput)

    #short_address = getAddressList(json_data["address"]["latitude"], json_data["address"]["longitude"])
    print('\n')
    print('All addresses:', short_address)

    return short_address
