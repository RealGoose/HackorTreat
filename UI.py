################################################################################
#Franz Kieviet
#franzkieviet@gmail.com
#10/31/2020
#This builds a simple UI for the user to use
################################################################################
from main import mainStructure
import webbrowser
from tkinter import *
window = Tk()

window.geometry("1000x700")
window.title("Garage Sales 4 You")
window.configure(bg='light blue')

header = Label(window, 
        bg= 'white',
        fg="light blue", 
        width=30,
        height=-10,
        anchor='s', 
        text = "Garage Sales 4 You!")
header.config(font =("Helvetica", 26, "bold")) 
header.place(x=175, y=20)

instructionsHeader = Label(window, 
        bg= 'light blue', 
        fg= "white",
        width=25,
        height=1,
        anchor='w', 
        text = "What is GS4Y?")
instructionsHeader.config(font =("Helvetica", 16, "bold")) 
instructionsHeader.place(x=0, y=70)

overview1 = Label(window,  
        bg="light blue",
        fg= "white",
        width=45,
        height=1,
        anchor='nw',
        justify="center",
        text = "-->Garage Sale 4 takes your location, searches popular")
overview1.config(font =("Helvetica", 11, "bold")) 
overview1.place(x=0, y=100)
overview2 = Label(window,  
        bg="light blue",
        fg= "white",
        width=45,
        height=1,
        anchor='nw',
        justify="center",
        text = "garage sale listing websites and gives you the best route!")
overview2.config(font =("Helvetica", 11, "bold")) 
overview2.place(x=0, y=120)


whyUseHeader = Label(window, 
        bg= 'light blue', 
        fg= "white",
        width=25,
        height=1,
        anchor='e', 
        text = "Why use GS4Y?")
whyUseHeader.config(font =("Helvetica", 16, "bold")) 
whyUseHeader.place(x=670, y=70)


overview1 = Label(window,  
        bg="light blue",
        fg= "white",
        width=45,
        height=1,
        anchor='nw',
        justify="center",
        text = "-->Garage Sale 4 You does all the work for you!!! But first")
overview1.config(font =("Helvetica", 11, "bold")) 
overview1.place(x=590, y=100)
overview2 = Label(window,  
        bg="light blue",
        fg= "white",
        width=45,
        height=1,
        anchor='e',
        justify="center",
        text = "pick a few settings to help tell GS4Y know your plans ")
overview2.config(font =("Helvetica", 11, "bold")) 
overview2.place(x=590, y=120)

divider = Label(window,  
        bg="white",
        fg= "white",
        width=800,
        height=-1,
        anchor='e',
        justify="center") 
divider.place(x=0, y=160)




dateHeader = Label(window,  
        bg="light blue",
        fg= "white",
        width=45,
        height=1,
        anchor='w',
        justify="center",
        text = "Date of trip:")
dateHeader.config(font =("Helvetica", 11, "bold")) 
dateHeader.place(x=0, y=180)


dayHeader = Label(window,  
        bg="light blue",
        fg= "white",
        width=60,
        height=1,
        anchor='w',
        justify="center",
        text = "Day:")
dayHeader.config(font =("Helvetica", 12)) 
dayHeader.place(x=0, y=200)
monthHeader = Label(window,  
        bg="light blue",
        fg= "white",
        width=60,
        height=1,
        anchor='w',
        justify="center",
        text = "Month:")
monthHeader.config(font =("Helvetica", 12)) 
monthHeader.place(x=0, y=221)
yearHeader = Label(window,  
        bg="light blue",
        fg= "white",
        width=60,
        height=1,
        anchor='w',
        justify="center",
        text = "Year:")
yearHeader.config(font =("Helvetica", 12)) 
yearHeader.place(x=0, y=243)


day=Entry(window)
day.place(x=60, y=200)
month=Entry(window)
month.place(x=60, y=223)
year=Entry(window)
year.place(x=60, y=246)


saleHeader = Label(window,  
        bg="light blue",
        fg= "white",
        width=45,
        height=1,
        anchor='w',
        justify="center",
        text = "How many garage sales would you like to go to?")
saleHeader.config(font =("Helvetica", 13, "bold")) 
saleHeader.place(x=315, y=200)

fiveSales=Radiobutton(window, text="5 Garage Sales",  bg="white", fg="light blue", height=2, width=15, indicatoron=0, command=lambda: Clicked(1))
fiveSales.place(x=300, y=243)
fiveSales.config(font =("Helvetica", 8, "bold"))

sixSales=Radiobutton(window, text="6 Garage Sales", bg="white", fg="light blue", height=2, width=15, indicatoron=0, command=lambda: Clicked(2))
sixSales.place(x=450, y=243)
sixSales.config(font =("Helvetica", 8, "bold"))

sevenSales=Radiobutton(window, text="7 Garage Sales", bg="white", fg="light blue",  height=2, width=15, indicatoron=0, command=lambda: Clicked(3))
sevenSales.place(x=600, y=243)
sevenSales.config(font =("Helvetica", 8, "bold"))


submit=Radiobutton(window, text="SUBMIT", bg="white", fg="light blue",  height=1, width=10, indicatoron=0, command=lambda: Clicked(4))
submit.place(x=800, y=300)
submit.config(font =("Helvetica", 16, "bold"))


#############################################   USER INPUTS:

dayInput=day.get()
monthInput=month.get()
yearInput=year.get()
date=str(yearInput)+"-"+str(monthInput)+"-"+str(dayInput)
numSales = 5

tableOfAddressesHEADER = Label(window,  
        bg="white",
        fg= "light blue",
        width=200,
        height=-1,
        text="LIST OF THE ADDRESSES:",
        anchor='w',
        justify="center") 
tableOfAddressesHEADER.place(x=0, y=400)
tableOfAddressesHEADER.config(font =("Helvetica", 16, "bold"))

tableOfAddresses = Label(window,  
        fg="white",
        bg= "light blue",
        width=200,
        height=-1,
        text="HOME #1",
        anchor='w',
        justify="center") 
tableOfAddresses.place(x=0, y=600)

location = mainStructure(numSales)

print(location)


locationWithPlus=[]
for i in range(5):
    for home in location:
        home.replace(' ', '+')
        home = str(home) + '\\'
        locationWithPlus.append(home)
    webbrowser.open('https://www.google.com/maps/dir/' + locationWithPlus[i])


tableOfAddressesFooter = Label(window,  
        bg="white",
        fg= "light blue",
        width=200,
        height=-1,
        text="Link to Google Map:" + 'https://www.google.com/maps/dir/' + locationWithPlus[0],
        anchor='w',
        justify="center") 
tableOfAddressesFooter.place(x=0, y=670)
tableOfAddressesFooter.config(font =("Helvetica", 16, "bold"))
numSales = 5

def Clicked(buttonStatus):
    if buttonStatus==1:
        numSales = 5
        mainStructure(numSales)
        
    elif buttonStatus==2:
        numSales = 6
        mainStructure(numSales)
        
    elif buttonStatus==3:
        numSales = 7
        mainStructure(numSales)
        
    elif buttonStatus==4:
        numSales = 5
        mainStructure(numSales)



window.mainloop() 
