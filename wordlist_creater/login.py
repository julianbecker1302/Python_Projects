
import sys

login = "B4aC"

l=[]
with open("list.txt","r") as file:
    for line in file:
        l.append(line[:-1])

for i in range(len(l)):
    sys.stdout.write("\rCompared " + str(i) + " out of " + str(len(l)))
    sys.stdout.flush()
    if l[i] == login:
        print("\nFound!: " + l[i])
        break
