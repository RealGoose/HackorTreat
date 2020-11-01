import http.client
import mimetypes
import json
from distanceRequest import getDistance
def getAddressList(latitude, longitude, location):

    latitude = 33.68460
    longitude = -117.82700
    """
    Prints a list of formatted addresses, change the "query" variable to the actual thing
    """
    location2 = []
    for j in location:
        j = j.replace(" ", "%20")
        location2.append(j)
        
    #print('\nlocation:', location)
    formatted_address_list = []
    
    for i in range(5):
        conn = http.client.HTTPSConnection("api.radar.io")
        payload = ''
        headers = {
          'Authorization': 'prj_test_pk_6e76504d47441be5e8ad2fc0dcd6daaa57083aa5 '
        }

        query = str(location2[i])
        #print('\n\n', location2[i], '\n\n')
        conn.request("GET", "/v1/search/autocomplete?query="+query+"&near=" + str(33.68460) + "," + str(-117.82700) + "&limit=1", payload, headers)
        res = conn.getresponse()
        
        data = res.read().decode("utf-8")

        json_data = json.loads(data)

        addresses = json_data["addresses"]

        d_list = []

        
        for address in addresses:
            formatted_address_list.append(address["formattedAddress"])
            d_list.append((address["latitude"],address["longitude"]))
            getDistance(latitude, longitude, address["latitude"], address["longitude"])

        #print("\nd_list:", d_list)
        #print("formatted_address_list", formatted_address_list)
    return formatted_address_list
