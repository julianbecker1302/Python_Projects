
import sys
import threading

class Comparator(threading.Thread):
    def __init__(self, liste, search, nmbr):
        threading.Thread.__init__(self)
        self.liste = liste
        self.search = search
        self.nmbr = nmbr
    
    def run(self):
        for i in range(len(self.liste)):
            if self.liste[i] == self.search:
                print("\nFound!: " + self.liste[i])
                break
        print(str(self.nmbr) + "thread finished")
        

login = "h3b6c"

l=[]
comparatorList = []

with open("list.txt","r") as file:
    for line in file:
        l.append(line[:-1])

x = input("How many threads")
x = int(x)



for i in range(int(x)):
    c1 = Comparator(l[int((len(l)/x)*i):int((len(l)/x)*(i+1))],login,i)
    comparatorList.append(c1)
    
for comparator in comparatorList:
    comparator.start()

for comparator in comparatorList:
    comparator.join()