from selenium import webdriver
import time


driver = webdriver.Chrome("/snap/bin/chromium.chromedriver")

songlist=[]


with open("eminem_songs.txt","r") as file:
    for line in file:
        songlist.append(line[:-1] + ", Eminem")



for song in songlist:
    try:
        if song != "":
            driver.get('https://docs.google.com/forms/d/e/1FAIpQLScTDpHwL0spR0CGXMkEX3hXOnzuOf2B8yBvpyRAVEfTIryOAA/viewform')
            textbox = driver.find_element_by_name("entry.1765775204")
            textbox.send_keys(song)
            sendebutton = driver.find_element_by_xpath("//div[@jsname='M2UYVd']")
            sendebutton.click()
    except:
        print("no")

driver.close()
