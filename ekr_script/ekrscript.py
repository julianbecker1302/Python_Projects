from selenium import webdriver
import requests
import os
import time



driver = webdriver.Chrome("/snap/bin/chromium.chromedriver")    #chromedriver path

driver.get("https://www.ebay-kleinanzeigen.de/m-einloggen.html?targetUrl=/")

#login with email and password
login_email = driver.find_element_by_id("login-email")
print("Insert your email")
mail = "nah"
login_pw = driver.find_element_by_id("login-password")
print("Insert your password")
pw = "you hoped, didn't you?"

login_email.send_keys(mail)
login_pw.send_keys(pw)

login_button = driver.find_element_by_id("login-submit")
login_button.click()



#
driver.get("https://www.ebay-kleinanzeigen.de/m-meine-anzeigen.html")
driver.find_element_by_xpath('//*[@id="my-manageads-adlist"]/li/article/footer/section[1]/ul/li[1]/a').click() #"bearbeiten"
driver.find_element_by_id("pstad-lnk-chngeCtgry").click()#"kategorie wählen"

print(driver.current_url)
