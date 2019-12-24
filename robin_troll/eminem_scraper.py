import requests
from bs4 import BeautifulSoup


response = requests.get("https://de.wikipedia.org/wiki/Liste_der_Lieder_von_Eminem")
soup = BeautifulSoup(response.text, "html.parser")

lieder = []

table = soup.find('table', {'class':'wikitable'})
td = table.findNext("td")


with open ("eminem_songs.txt", "w") as file:
    for i in range(500):
        tr = td.findNext("tr")
        td = tr.findNext("td", text=True)
        file.write(str(td)[4:-5])  #remove html-tags
