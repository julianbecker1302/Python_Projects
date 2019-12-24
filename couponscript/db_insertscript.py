from selenium import webdriver
import time


wd = webdriver.Chrome("/snap/bin/chromium.chromedriver")    #chromedriver path

l =[]

with open("codes.txt" ,"r") as file:
    for line in file:
        l.append(line)



wd.get("https://douchebags.com/the-scholar-doyoutravel-gypsea-lust")



time.sleep(10)

for line in l:
    try:
        time.sleep(2)
        dc_form = wd.find_elements_by_name("discountCode")
        dc_form[1].send_keys(line)
        ap_button = wd.find_elements_by_xpath("//button[text()='Apply']")
        ap_button[1].click()
    except:
        wd.refresh()
