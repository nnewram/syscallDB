import requests
import urllib.request
from bs4 import BeautifulSoup
import pickle

url = "https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
syscalls = soup.findAll("tr")[1:]
sysdict = {}

for syscall in syscalls:
    sysarr = str(syscall).split("</td><td>")
    sysarr[0] = int(sysarr[0].split(">")[-1])
    sysarr = [x for x in sysarr if "<" not in str(x) and x != ""]
    sysdict[sysarr[0]] = sysarr[1:]
print(sysdict)

with open("../scrapedx86.pickle", "wb") as pickleHandle:
    pickle.dump(sysdict, pickleHandle, protocol=pickle.HIGHEST_PROTOCOL)
print("done")
