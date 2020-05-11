from bs4 import BeautifulSoup
import pickle

with open("latest.html", "r") as f:
    contents = f.read()
soup = BeautifulSoup(contents, "html.parser")
syscalls = soup.findAll("tr")[2:]
sysdict = {}

for syscall in syscalls:
    sysarr = [str(syscall).split("</a>")[0].split(">")[-1]] + str(syscall).replace("</td>", "").replace("\n", "").split("<td>")[2:9]
    sysarr[0] = "sys_" + sysarr[0]
    sysdict[int(str(syscall).split("</th>")[0].split(">")[-1])] = sysarr

[print(sysdict[x]) for x in sysdict]

with open("../../scrapedarm64.pickle", "wb") as pickleHandle:
    pickle.dump(sysdict, pickleHandle, protocol=pickle.HIGHEST_PROTOCOL)

print("done")
