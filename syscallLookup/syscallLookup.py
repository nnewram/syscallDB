import pickle
import sys

bitwidth = 64
if "-x64" in sys.argv or "-32" in sys.argv:
    bitwidth = 32
    with open("scrapedx64.pickle", "rb") as scrapeHandle:
        scraped = pickle.load(scrapeHandle)
else:
    with open("scrapedx86.pickle", "rb") as scrapeHandle:
        scraped = pickle.load(scrapeHandle)

def printSyscall(key):
    if bitwidth == 64:
        try:
            print("")
            print("syscall: " + scraped[key][0])
            print("rax: " + str(key))
            print("rdi: " + scraped[key][1])
            print("rsi: " + scraped[key][2])
            print("rdx: " + scraped[key][3])
            print("r10: " + scraped[key][4])
            print("r8: " + scraped[key][5])
            print("r9: " + scraped[key][6])
        except:
            pass
    else:
        try:
            print("")
            print("syscall: " + scraped[key][1])
            print("eax: " + str(key))
            print("ebx: " + scraped[key][4])
            print("ecx: " + scraped[key][5])
            print("edx: " + scraped[key][6])
            print("esi: " + scraped[key][7])
            print("edi: " + scraped[key][8])
        except:
            pass

if "--reverse" in sys.argv or "-r" in sys.argv:
    toSearch = input("Syscall: ").lower()
    if bitwidth == 32:
        reverse = {v[1]: k for k, v in scraped.items()}
    else:
        reverse = {v[0]: k for k, v in scraped.items()}
    key = 0
    for x in reverse:
        if toSearch in x.lower():
            printSyscall(key)
            key += 1
            continue
        key += 1
else:
    index = int(input("Syscall number: "))
    printSyscall(index)
