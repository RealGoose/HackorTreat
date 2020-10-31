# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#User zipcode
zipcode=92620 #Change this later



# Set URL's for all of our garage sale websites
    #GarageSaleTracker.com              GST
urlGST = 'https://www.garagesalestracker.com/garage-sale-' + str(zipcode) +'.html'
    #yardsalesearch.com                 YSS
urlYSS='https://www.yardsalesearch.com/garage-sales.html?zip='+str(zipcode)

#Will expand to more websites



#Get the webpage
responseGST = requests.get(urlGST)
#responseYSS = requests.get(urlYSS)



#Parse HTML by using BeautifulSoup(Datatype=BeautifulSoup Object)
GSTasSoupOBJ = BeautifulSoup(responseGST.text, "html.parser")
#YSSasSoupOBJ = BeautifulSoup(responseYSS.text, "html.parser")


#Collect the sale info from each site, and store it as an object. 
    #Date, Address

#height = soup.find(class_ = 'item height').find('strong').get_text()
#GST:
#print(GSTasSoupOBJ)
#print(GSTasSoupOBJ.findAll('p'))
w=[]
location=[]
dates=[]
x=GSTasSoupOBJ.findAll('p')
z=0
for address in x:
    address=str(address)
    q=address.partition("<span")[0]
    w.append(q)
    e=q[38:] #removed space
    location.append(e.partition("<br")[0])
    #Now lets take the date:
    r=q.partition("<br")[2] #Remove location part
    t=r[35:]
    dates.append(t.partition("<br")[0])

print(dates)
#print(str(address))
#print(GSTasSoupOBJ.find('div', class_="small-12 medium-7 columlns sale-details"))
#print(GSTasSoupOBJ.find("span", itemprop="streetAddress"))