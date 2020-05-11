def _syscallLookup(key, arch, scraped=""):
    if scraped == "":
        if "pickle" not in locals():
            import pickle
        
        if arch == "i386":
            with open("syscallLookup/scrapedx64.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
        
        elif arch == "x86_64":
            with open("syscallLookup/scrapedx86.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
        
        elif arch == "arm64":
            with open("syscallLookup/scrapedArm64.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
        
        elif arch == "powerPC":
            with open("syscallLookup/scrapedpowerpc.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
        
        elif arch == "mips64":
            with open("syscallLookup/scrapedmips64.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
    
    collected = {}
    
    selectedSyscall = scraped[key]
    if arch == "i386":
        collected["syscall"] = selectedSyscall[1]
        collected["eax"] = key
        collected["ebx"] = selectedSyscall[4]
        collected["ecx"] = selectedSyscall[5]
        collected["edx"] = selectedSyscall[6]
        collected["esi"] = selectedSyscall[7]
        collected["edi"] = selectedSyscall[8]
    
    elif arch == "x86_64":
        try:
            collected["syscall"] = selectedSyscall[0]
            collected["rax"] = key
            collected["rdi"] = selectedSyscall[1]
            collected["rsi"] = selectedSyscall[2]
            collected["rdx"] = selectedSyscall[3]
            collected["r10"] = selectedSyscall[4]
            collected["r8"] = selectedSyscall[5]
            collected["r9"] = selectedSyscall[6]
        except:
            pass
    
    elif arch == "arm64":
        collected["syscall"] = selectedSyscall[0]
        collected["x8"] = selectedSyscall[1]
        collected["x0"] = selectedSyscall[2]
        collected["x1"] = selectedSyscall[3]
        collected["x2"] = selectedSyscall[4]
        collected["x3"] = selectedSyscall[5]
        collected["x4"] = selectedSyscall[6]
        collected["x5"] = selectedSyscall[7]

    elif arch == "powerPC":
        collected["syscall"] = selectedSyscall[0]
        collected["r0"] = key
        collected["r3"] = selectedSyscall[1]
        collected["r4"] = selectedSyscall[2]
        collected["r5"] = selectedSyscall[3]
        collected["r6"] = selectedSyscall[4]
        collected["r7"] = selectedSyscall[5]
        collected["r8"] = selectedSyscall[6]

    elif arch == "mips64":
        collected["syscall"] = selectedSyscall[0]
        collected["v0"] = key
        collected["a0"] = selectedSyscall[1]
        collected["a1"] = selectedSyscall[2]
        collected["a2"] = selectedSyscall[3]
        collected["a3"] = selectedSyscall[4]
        collected["a4"] = selectedSyscall[5]
        collected["a5"] = selectedSyscall[6]

    return collected

def _reverseLookup(string, arch):
    if "pickle" not in locals():
        import pickle

    if arch == "i386":
        with open("syscallLookup/scrapedx64.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[1]: k for k, v in scraped.items()}
    
    elif arch == "x86_64":
        with open("syscallLookup/scrapedx86.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}
    
    elif arch == "arm64":
        with open("syscallLookup/scrapedArm64.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}
    
    elif arch == "powerPC":
        with open("syscallLookup/scrapedpowerpc.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}

    elif arch == "mips64":
        with open("syscallLookup/scrapedmips64.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]:k for k, v in scraped.items()}

    syscalls = []
    key = 0
    reverseMax = max(scraped)

    for x in reverse:
        while key not in scraped and key < reverseMax:
            key += 1 # index might skip sometimes

        if string in x.lower():
            syscalls.append(_syscallLookup(key, arch, scraped))
        
        key += 1

    return syscalls

def syscall32(query="sys"):
    if type(query) == str:
        return _reverseLookup(query, "i386")
    elif type(query) == int:
        return _syscallLookup(query, "i386")
    raise Exception("Invalid type: " + str(type(query)))

def syscall64(query):
    if type(query) == str:
        return _reverseLookup(query, "x86_64")
    elif type(query) == int:
        return _syscallLookup(query, "x86_64")
    raise Exception("Invalid type: " + str(type(query)))

def syscallArm64(query):
    if type(query) == str:
        return _reverseLookup(query, "arm64")
    elif type(query) == int:
        return _syscallLookup(query, "arm64")
    raise Exception("Invalid type: " + str(type(query)))

def syscallPPC(query):
    if type(query) == str:
        return _reverseLookup(query, "powerPC")
    elif type(query) == int:
        return _syscallLookup(query, "powerPC")
    raise Exception("Invalid type: " + str(type(query)))

def syscallMips64(query): #this is n64
    if type(query) == str:
        return _reverseLookup(query, "mips64")
    elif type(query) == int:
        return _syscallLookup(query, "mips64")
    raise Exception("Invalid type: " + str(type(query)))
