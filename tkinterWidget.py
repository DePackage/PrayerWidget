# Import Modules
import tkinter as tk
import requests
import time


from bs4 import BeautifulSoup
from screeninfo import get_monitors

Prayer_time_based_on_country_URL = 'https://www.islamicfinder.org/prayer-widget/248946/shafi/4/0/18.5/19.0'
icon = "OrangePrayerMat.ico"

def getPrayerTimes():
    html_request = requests.get(Prayer_time_based_on_country_URL)
    soup = BeautifulSoup(html_request.text, 'html.parser')

    Fajr = soup.find_all(text="Fajr")
    Fajr = Fajr[0].parent.text.split("\n")[1].split()[0].split(":")
    Fajr = int(Fajr[0])*60 + int(Fajr[1])

    Sunrise = soup.find_all(text="Sunrise  ")
    Sunrise = Sunrise[0].parent.text.split("\n")[1].split()[0].split(":")
    Sunrise = int(Sunrise[0])*60 + int(Sunrise[1])

    Dhuhr = soup.find_all(text="Dhuhr")
    Dhuhr = Dhuhr[0].parent.text.split("\n")[1].split()[0].split(":")
    if(Dhuhr[1] == "PM"): 
        Dhuhr = int((Dhuhr[0])+12)*60 + int(Dhuhr[1])
    else:
        Dhuhr = int(Dhuhr[0])*60 + int(Dhuhr[1])

    Asr = soup.find_all(text="Asr")
    Asr = Asr[0].parent.text.split("\n")[1].split()[0].split(":")
    Asr = (int(Asr[0])+12)*60 + int(Asr[1])

    Maghrib = soup.find_all(text="Maghrib")
    Maghrib = Maghrib[0].parent.text.split("\n")[1].split()[0].split(":")
    Maghrib = (int(Maghrib[0])+12)*60 + int(Maghrib[1])

    Isha = soup.find_all(text="Isha")
    Isha = Isha[0].parent.text.split("\n")[1].split()[0].split(":")
    Isha = (int(Isha[0])+12)*60 + int(Isha[1])

    return(Fajr,Sunrise,Dhuhr,Asr,Maghrib,Isha)

def getInfo(prayer):
    name = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"]
    now = time.gmtime()
    now = ((now[3] + 3)%24)*60 + now[4]
    pray = "default"
    mins = 99
    if now > prayer[5]:
        pray = name[0]
        mins = prayer[0] - now + 1440
    else:
        for i in range(6):
            if now < prayer[i] + 30:
                pray = name[i]
                mins = prayer[i] - now
    text = "{}:{}".format(pray,mins)
    return text

def loop():
    info = getInfo(prayer)
    print(info)
    counter.config(text = info) 
    root.after(30000, loop)


# Window Location
monitor = get_monitors()
prayer = getPrayerTimes()
width = 120
height = 20
geo = "{}x{}+{}+{}".format(width,height,monitor[0].width-width - 40,0)

# Create Object
root = tk.Tk()
root.title('Prayer Times') 
root.iconbitmap(icon)
root.overrideredirect(1)

# Set Geometry and Attributes
root.configure(background='#333333')
root.attributes('-alpha', 0.75)
root.attributes('-topmost',True)
root.geometry(geo)

# Text
counter = tk.Label(root,bg ='#333333',fg = "orange", text = "", font=('Helvetica bold', 12))
counter.pack()

root.after(1000, loop)
tk.mainloop()
# Execute Tkinter
root.mainloop()