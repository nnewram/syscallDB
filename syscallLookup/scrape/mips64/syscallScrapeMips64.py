import requests
from bs4 import BeautifulSoup
import pickle

url = "https://syscalls.w3challs.com/?arch=mips_n64"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
syscalls = soup.findAll("tr")[2:]
sysdict = {}

for syscall in syscalls:
    sysarr = ["sys_" + str(syscall).split("</td><td>")[1].split("</a>")[0].split(">")[-1]]
    sysarr += str(syscall).split("</td><td>")[3:9]
    sysarr = [x if "<a" not in x else x.split("</a>")[0].split(">")[-1] for x in sysarr]
    sysarr = [x if x != "-" else "" for x in sysarr]
    syscallnumber = int(str(syscall).split("<td>")[1].split("</td>")[0])
    sysdict[syscallnumber] = sysarr

for x in sysdict:
    print(sysdict[x])

with open("../../scrapedmips64.pickle", "wb") as pickleHandle:
    pickle.dump(sysdict, pickleHandle, protocol=pickle.HIGHEST_PROTOCOL)
print("done")
