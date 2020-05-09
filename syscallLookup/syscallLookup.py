import pickle
import sys

with open("scraped.pickle", "rb") as scrapeHandle:
    scraped = pickle.load(scrapeHandle)

def printSyscall(key):
    try:
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
if "--reverse" in sys.argv or "-r" in sys.argv:
    toSearch = input("Syscall: ").lower()
    reverse = {v[0]: k for k, v in scraped.items()}
    key = 0
    for x in reverse:
        if toSearch in x.lower():
            break 
        key += 1
    else:
        print("Not found")
        exit(1)
    printSyscall(key)
else:
    index = int(input("Syscall number: "))
    printSyscall(index)
    #"rax", "syscall", "rdi", "rsi", "rdx", "r10", "r8", "r9"
