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
from apiCalls import getAddressList


def WebScrapper(zipcode, latitude, longtitude, dateInput): 

    #User zipcode
    zipcode=92614 

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
        dateRaw=dateNoSpace.partition("<br")[0]
        #dates.append(dateNoSpace.partition("<br")[0])
        if "Jan" in dateRaw:
            index=dateRaw.find("Jan")
            dateStr="2020"+"-01-"+dateRaw[index+4:index+6]
        elif "Feb" in dateRaw:
            index=dateRaw.find("Feb")
            dateStr="2020"+"-02-"+dateRaw[index+4:index+6]
        elif "Mar" in dateRaw:
            index=dateRaw.find("Mar")
            dateStr="2020"+"-03-"+dateRaw[index+4:index+6] 
        elif "Apr" in dateRaw:
            index=dateRaw.find("Apr")
            dateStr="2020"+"-04-"+dateRaw[index+4:index+6] 
        elif "May" in dateRaw:
            index=dateRaw.find("May")
            dateStr="2020"+"-05-"+dateRaw[index+4:index+6] 
        elif "June" in dateRaw:
            index=dateRaw.find("June")
            dateStr="2020"+"-06-"+dateRaw[index+4:index+6] 
        elif "Jul" in dateRaw:
            index=dateRaw.find("Jul")
            dateStr="2020"+"-07-"+dateRaw[index+4:index+6] 
        elif "Aug" in dateRaw:
            index=dateRaw.find("Aug")
            dateStr="2020"+"-08-"+dateRaw[index+4:index+6] 
        elif "Sep" in dateRaw:
            index=dateRaw.find("Sep")
            dateStr="2020"+"-09-"+dateRaw[index+4:index+6] 
        elif "oOt" in dateRaw:
            index=dateRaw.find("Nov")
            dateStr="2020"+"-10-"+dateRaw[index+4:index+6] 
        elif "Nov" in dateRaw:
            index=dateRaw.find("Nov")
            dateStr="2020"+"-11-"+dateRaw[index+4:index+6] 
        elif "Dec" in dateRaw:
            index=dateRaw.find("Dec")
            dateStr="2020"+"-12-"+dateRaw[index+4:index+6]
        indexSpace=dateStr.find(" ")
        dateStr=dateStr[0:-2]+"0"+dateStr[indexSpace+1:indexSpace+2]    
        dates.append(dateStr)

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



    ### REMOVE ALL THE DATES THAT DON'T MEET OUR DATE ###
    z=0
    locationToReturn=[]
    for i in dates:
        if(i==dateInput):
            locationToReturn.append(location[z])
            z=z+1
        else:
            z=z+1

    formatted_address_list = getAddressList(latitude, longtitude, locationToReturn)
    return locationToReturn, formatted_address_list


    print(locationToReturn)
