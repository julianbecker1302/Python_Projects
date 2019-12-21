
import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.discographien.de/alle_songs_von_Kollegah.htm")
soup = BeautifulSoup(response.text, "html.parser")


l = soup.findAll('a')
ergebnis = []

for line in l:
    ergebnis.append(str(line(text=True))[3:-2])

endeergebnis = []

for i in range(len(ergebnis)):
    if (i % 3 == 0):
        endeergebnis.append(ergebnis[i])

with open("alle_songs_von_Kollegah.txt", "w") as file:
    for line in ergebnis:
        file.write(str(line) + "\n")
