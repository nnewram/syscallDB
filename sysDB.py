def _syscallLookup(key, bitwidth, scraped=""):
    if scraped == "":
        if "pickle" not in locals():
            import pickle
        if bitwidth == 32:
            with open("syscallLookup/scrapedx64.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
            reverse = {v[1]: k for k, v in scraped.items()}
        else:
            with open("syscallLookup/scrapedx86.pickle", "rb") as scrapeHandle:
                scraped = pickle.load(scrapeHandle)
            reverse = {v[0]: k for k, v in scraped.items()}
    
    collected = {}
    if bitwidth == 32:
        collected["syscall"] = scraped[key][1]
        collected["eax"] = key
        collected["ebx"] = scraped[key][4]
        collected["ecx"] = scraped[key][5]
        collected["edx"] = scraped[key][6]
        collected["esi"] = scraped[key][7]
        collected["edi"] = scraped[key][8]
    else:
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
    return collected
def _reverseLookup(string, bitwidth):
    if "pickle" not in locals():
        import pickle

    if bitwidth == 32:
        with open("syscallLookup/scrapedx64.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[1]: k for k, v in scraped.items()}
    else:
        with open("syscallLookup/scrapedx86.pickle", "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}
    
    syscalls = []
    key = 0

    for x in reverse:
        if string in x.lower():
            syscalls.append(_syscallLookup(key, bitwidth, scraped))
            key += 1
            continue
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