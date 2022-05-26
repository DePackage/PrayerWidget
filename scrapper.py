from re import S
import requests
import time
from bs4 import BeautifulSoup

#using https://www.islamicfinder.org/widgets/#prayertimeswidget
Prayer_time_based_on_country_URL = 'https://www.islamicfinder.org/prayer-widget/248946/shafi/4/0/18.5/19.0'

while True:
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

    F = 1
    S = 1
    D = 1
    A = 1
    Ma = 1
    I = 1

    while F:    
        now = time.gmtime()
        H = (now[3] + 3)%24
        M = now[4]
        if H*60 + M >= Fajr:
            F = 0
            break
        print("{Fajr:{}".format(Fajr -(H*60 + M)))
        time.sleep(30)

    while S:    
        now = time.gmtime()
        H = (now[3] + 3)%24
        M = now[4]
        if H*60 + M >= Sunrise:
            S = 0
            break 
        print("Sunrise:{}".format(Sunrise -(H*60 + M)))
        time.sleep(30)

    while D:    
        now = time.gmtime()
        H = (now[3] + 3)%24
        M = now[4]
        if H*60 + M >= Dhuhr:
            D = 0
            break
        print("Dhuhr:{}".format(Dhuhr -(H*60 + M)))
        time.sleep(30)


    while A:    
        now = time.gmtime()
        H = (now[3] + 3)%24
        M = now[4] 
        if H*60 + M >= Asr:
            A = 0
            break
        print("Asr:{}".format(Asr -(H*60 + M)))
        time.sleep(30)

    while Ma:    
        now = time.gmtime()
        H = (now[3] + 3)%24
        M = now[4]
        if H*60 + M >= Maghrib:
            Ma = 0
            break
        print("Maghrib:{}".format(Maghrib -(H*60 + M)))
        time.sleep(30)

    while I:    
        now = time.gmtime()
        H = (now[3] + 3)%24
        M = now[4] 
        if H*60 + M >= Isha:
            I = 0
            break
        print("Isha:{}".format(Isha -(H*60 + M)))
        time.sleep(30)

    F = 1
    S = 1
    D = 1
    A = 1
    Ma = 1
    I = 1
