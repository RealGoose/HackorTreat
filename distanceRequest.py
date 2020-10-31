import http.client
import mimetypes
import json

def getDistance(olat, olong, dlat, dlong):
    """
    Returns a tuple of the distance and the time in miles and minutes
    """
    conn = http.client.HTTPSConnection("api.radar.io")
    payload = ''
    headers = {
      'Authorization': 'prj_test_pk_6e76504d47441be5e8ad2fc0dcd6daaa57083aa5 ',
      'Cookie': '__cfduid=d981d1241b45417a69a90d4b31bdd8b0b1601077696'
    }
    conn.request("GET", "/v1/route/distance?origin=" + str(olat) + "," + str(olong) + "&destination=" + str(dlat) + ',' +  str(dlong) + "&modes=car&units=imperial", payload, headers)
    res = conn.getresponse()
    data = res.read()
    #print(data.decode("utf-8"))
