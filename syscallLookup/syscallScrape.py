import requests
import urllib.request
from bs4 import BeautifulSoup
import pickle

url = "https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
syscalls = soup.findAll("tr")[1:]
sysdict = {}

def separate(text):
    i = 0
    while (ord(text[i]) >= 48) and (ord(text[i]) <= 57):
        i += 1
    numberPart = text[:i]
    textPart = text[i:]
    return int(numberPart), textPart

for syscall in syscalls:
        number, text = separate(syscall.text)
        sysdict[number] = text.split(" ")
print(sysdict)

with open("scraped.pickle", "wb") as pickleHandle:
    pickle.dump(sysdict, pickleHandle, protocol=pickle.HIGHEST_PROTOCOL)
print("done")
