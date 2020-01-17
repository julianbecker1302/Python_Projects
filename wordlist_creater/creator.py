import os
import string

chr_lower = string.ascii_lowercase + "0123456789"

s=""

for i in range(36):
    for j in range(36):
        for k in range(36):
            for l in range(36):
                for m in range(36):
                        s += chr_lower[i]+chr_lower[j]+chr_lower[k]+chr_lower[l]+chr_lower[m]+"\n"

with open("list.txt", "w") as file:
    file.write(s)
