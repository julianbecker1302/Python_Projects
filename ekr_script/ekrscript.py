from selenium import webdriver
import os



driver = webdriver.Chrome("/snap/bin/chromium.chromedriver")    #chromedriver path

driver.get("https://www.ebay-kleinanzeigen.de/s-anzeige/oneplus-3t/1288055970-173-7986")

login_email = driver.find_element_by_id("login-email")
print("Insert your email")
mail = input(">")
login_pw = driver.find_element_by_id("login-password")
print("Insert your password")
pw = input(">")

login_email.send_keys(mail)
login_pw.send_keys(pw)

login_button = driver.find_element_by_id("login-submit")
login_button.click()

driver.get("https://www.ebay-kleinanzeigen.de/m-meine-anzeigen.html")
