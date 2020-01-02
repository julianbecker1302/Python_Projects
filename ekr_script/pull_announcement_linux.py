from bs4 import BeautifulSoup
import requests
import os
import urllib.request

#link = input("Insert Link of Announcement:")
link = "https://www.ebay-kleinanzeigen.de/s-anzeige/oneplus-3t/1288055970-173-7986"
print("\nExtracting from " + link + "\n\n")
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")

pic_links = []

pic_list = soup.find(id="viewad-thumbnail-list")
for line in pic_list.find_all("img"):
    pic_links.append(line["data-imgsrc"])

print("------------------------------------------------------------------------")
print('Beginning to download the the ad images...\n')


for i in range(len(pic_links)):
    print("Download " + link +"...")
    urllib.request.urlretrieve(pic_links[i], os.getcwd()+"/resources/pic" + str(i+1)+".jpg")       #works for linux filesystem!!!

                                                                                            #not windows!!
print("\nImages downloaded\n")
print("------------------------------------------------------------------------")
print("Extracting ad title...\n")


title = soup.find(id="viewad-title")
with open(os.getcwd()+"/resources/infos.txt", "w") as file:
    file.write(title.text.strip()+"\n")


    print("Title:\n" +title.text.strip())
    print("\nTitle file created\n")
    print("------------------------------------------------------------------------")
    print("Extracting ad description...\n")


    description = soup.find(id="viewad-description-text")
    file.write(description.text.strip()+"\n")


    print("Text:\n" +description.text.strip())
    print("\nDescription file created")
    print("------------------------------------------------------------------------")
    print("Extracting price...\n")


    price_text = soup.find(id="viewad-price").text.strip().split()
    price = price_text[1]


    print(price)
    print("\nPrice extracted")
    file.write(price)
