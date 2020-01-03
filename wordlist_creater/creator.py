import os
import string

n = int(input("How many characters?"))

chr_lower = string.ascii_lowercase + string.ascii_uppercase + "0123456789"

s=""

for i in range(62):
    for j in range(62):
        for k in range(62):
            s += chr_lower[i]+chr_lower[j]+chr_lower[k]+"\n"

with open("list.txt", "w") as file:
    file.write(s)
