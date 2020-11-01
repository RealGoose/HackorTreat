################################################################################
#Franz Kieviet
#franzkieviet@gmail.com
#10/31/2020
#This is a web scrapper that has present garage sale websites 
#and takes the dates and location of the sales.
################################################################################


# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#User zipcode
def WebScrapper(zipcode): 


    # Set URL's for all of our garage sale websites
        #GarageSaleTracker.com              GST
    urlGST = 'https://www.garagesalestracker.com/garage-sale-' + str(zipcode) +'.html'
        #yardsalesearch.com                 YSS
    urlYSS='https://www.yardsalesearch.com/garage-sales.html?zip='+str(zipcode)


    #Get the webpage
    responseGST = requests.get(urlGST)
    responseYSS = requests.get(urlYSS)

    #Parse HTML by using BeautifulSoup(Datatype=BeautifulSoup Object)
    GSTasSoupOBJ = BeautifulSoup(responseGST.text, "html.parser")
    YSSasSoupOBJ = BeautifulSoup(responseYSS.text, "html.parser")


    #Collect the sale info from each site, and store it as in its own array
    location=[]
    dates=[]


    #GST:
    for address in GSTasSoupOBJ.findAll('p'):
        #Take just the adress and date
        address=str(address)
        rawLocationAddress=address.partition("<span")[0]

        #Take just location
        locationNoSpace=rawLocationAddress[38:] #removed space
        location.append(locationNoSpace.partition("<br")[0])

        #Now lets take the date:
        dateNoLocationWithSpace=rawLocationAddress.partition("<br")[2] #Remove location part
        dateNoSpace=dateNoLocationWithSpace[35:] #removed space
        dates.append(dateNoSpace.partition("<br")[0])

    #YSS
    for address in YSSasSoupOBJ.findAll('span', itemprop="streetAddress"):
        #Take just the address
        address=str(address)
        rawLocationAddress=address.partition(">")[2]

        #Take just location
        location.append(rawLocationAddress.partition("</span")[0])



    for date in YSSasSoupOBJ.findAll('meta', itemprop="startDate"):
        #Take just the date
        date=str(date)
        rawDate=date.partition("=\"")[2]

        #Take just location
        dates.append(rawDate.partition("\" ")[0])
    
    
    return location
