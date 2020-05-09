import requests
import urllib.request
from bs4 import BeautifulSoup
import pickle

url = "http://syscalls.kernelgrok.com/syscalls-2.6.35.4.js"

response = requests.get(url)
syscalls = response.json()["aaData"]
cleanedSyscalls = {}
i = 0
for syscall in syscalls:
    if syscall[1] == "not implemented":
        continue
    sc = []
    for x in syscall:
        if type(x) == str and "/" in x:
            break
        if type(x) == dict:
            sc.append(x["type"])
            continue
        sc.append(x)
    cleanedSyscalls[i] = sc
    i += 1
print(cleanedSyscalls)

with open("../scrapedx64.pickle", "wb") as pickleHandle:
    pickle.dump(cleanedSyscalls, pickleHandle, protocol=pickle.HIGHEST_PROTOCOL)
print("done")
