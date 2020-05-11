def _syscallLookup(key, arch, scraped=""):
    if scraped == "":
        if "pickle" not in locals():
            import pickle
        
        if arch == 32:
            with open("syscallLookup/scrapedx64.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
        
        elif arch == 64:
            with open("syscallLookup/scrapedx86.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
        
        elif arch == "arm64":
            with open("syscallLookup/scrapedArm64.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
    
    collected = {}
    
    if arch == 32:
        collected["syscall"] = scraped[key][1]
        collected["eax"] = key
        collected["ebx"] = scraped[key][4]
        collected["ecx"] = scraped[key][5]
        collected["edx"] = scraped[key][6]
        collected["esi"] = scraped[key][7]
        collected["edi"] = scraped[key][8]
    
    elif arch == 64:
        try:
            collected["syscall"] = scraped[key][0]
            collected["rax"] = key
            collected["rdi"] = scraped[key][1]
            collected["rsi"] = scraped[key][2]
            collected["rdx"] = scraped[key][3]
            collected["r10"] = scraped[key][4]
            collected["r8"] = scraped[key][5]
            collected["r9"] = scraped[key][6]
        except:
            pass
    
    elif arch == "arm64":
        collected["syscall"] = scraped[key][0]
        collected["x8"] = scraped[key][1]
        collected["x0"] = scraped[key][2]
        collected["x1"] = scraped[key][3]
        collected["x2"] = scraped[key][4]
        collected["x3"] = scraped[key][5]
        collected["x4"] = scraped[key][6]
        collected["x5"] = scraped[key][7]

    return collected

def _reverseLookup(string, arch):
    if "pickle" not in locals():
        import pickle

    if arch == 32:
        with open("syscallLookup/scrapedx64.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[1]: k for k, v in scraped.items()}
    
    elif arch == 64:
        with open("syscallLookup/scrapedx86.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}
    
    elif arch == "arm64":
        with open("syscallLookup/scrapedArm64.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}
    
    syscalls = []
    key = 0
    reverseMax = max(scraped)

    for x in reverse:
        while not scraped.get(key) and key < reverseMax:
            key += 1 # index might skip sometimes

        if string in x.lower():
            syscalls.append(_syscallLookup(key, arch, scraped))
        
        key += 1

    return syscalls

def syscall32(query="sys"):
    if type(query) == str:
        return _reverseLookup(query, 32)
    elif type(query) == int:
        return _syscallLookup(query, 32)
    raise Exception("Invalid type: " + str(type(query)))

def syscall64(query):
    if type(query) == str:
        return _reverseLookup(query, 64)
    elif type(query) == int:
        return _syscallLookup(query, 64)
    raise Exception("Invalid type: " + str(type(query)))

def syscallarm64(query):
    if type(query) == str:
        return _reverseLookup(query, "arm64")
    elif type(query) == int:
        return _syscallLookup(query, "arm64")
    raise Exception("Invalid type: " + str(type(query)))
