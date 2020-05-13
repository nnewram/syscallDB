def _syscallLookup(key, arch, scraped=None):
    if not scraped:
        if "pickle" not in locals():
            import pickle
    
        if "os" not in locals():
            import os
        
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        with open(os.path.join(location, "syscallLookup/scraped%s.pickle" % arch), "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)

    collected = {}
    
    selectedSyscall = scraped[key]
    if arch == "i386":
        collected["int 0x80"] = selectedSyscall[1]
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

    elif arch == "x86_32":
        try:
            collected["syscall"] = selectedSyscall[0]
            collected["ax"] = key
            collected["di"] = selectedSyscall[1]
            collected["si"] = selectedSyscall[2]
            collected["dx"] = selectedSyscall[3]
            collected["r10w"] = selectedSyscall[4]
            collected["r8w"] = selectedSyscall[5]
            collected["r9w"] = selectedSyscall[6]
        except:
            pass

    elif arch == "arm64":
        collected["svc #0"] = selectedSyscall[0]
        collected["x8"] = selectedSyscall[1]
        collected["x0"] = selectedSyscall[2]
        collected["x1"] = selectedSyscall[3]
        collected["x2"] = selectedSyscall[4]
        collected["x3"] = selectedSyscall[5]
        collected["x4"] = selectedSyscall[6]
        collected["x5"] = selectedSyscall[7]

    elif arch == "powerPC":
        collected["sc"] = selectedSyscall[0]
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
    
    elif arch == "mips32":
        collected["syscall"] = selectedSyscall[0]
        collected["v0"] = key
        collected["a0"] = selectedSyscall[1]
        collected["a1"] = selectedSyscall[2]
        collected["a2"] = selectedSyscall[3]
        collected["a3"] = selectedSyscall[4]
        collected["a4"] = selectedSyscall[5]
        collected["a5"] = selectedSyscall[6]
    
    elif arch == "mipso32":
        collected["syscall"] = selectedSyscall[0]
        collected["v0"] = key
        collected["a0"] = selectedSyscall[1]
        collected["a1"] = selectedSyscall[2]
        collected["a2"] = selectedSyscall[3]
        collected["a3"] = selectedSyscall[4]
        collected["stack1"] = selectedSyscall[5]
        collected["stack2"] = selectedSyscall[6]

    elif arch == "sparc64":
        collected["t 0x6d"] = selectedSyscall[0]
        collected["g1"] = key
        collected["o0"] = selectedSyscall[1]
        collected["o1"] = selectedSyscall[2]
        collected["o2"] = selectedSyscall[3]
        collected["o3"] = selectedSyscall[4]
        collected["o4"] = selectedSyscall[5]
        collected["o5"] = selectedSyscall[6]
    
    elif arch == "sparc32":
        collected["t 0x10"] = selectedSyscall[0]
        collected["g1"] = key
        collected["o0"] = selectedSyscall[1]
        collected["o1"] = selectedSyscall[2]
        collected["o2"] = selectedSyscall[3]
        collected["o3"] = selectedSyscall[4]
        collected["o4"] = selectedSyscall[5]
        collected["o5"] = selectedSyscall[6]
    
    elif arch == "ia64":
        collected["break 0x100000"] = selectedSyscall[0]
        collected["r15"] = key
        collected["out0"] = selectedSyscall[1]
        collected["out1"] = selectedSyscall[2]
        collected["out2"] = selectedSyscall[3]
        collected["out3"] = selectedSyscall[4]
        collected["out4"] = selectedSyscall[5]
        collected["out5"] = selectedSyscall[6]

    return collected

def _reverseLookup(string, arch, startingsyscall=0):
    if "pickle" not in locals():
        import pickle
    
    if "os" not in locals():
        import os
    
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    if arch == "i386":
        with open(os.path.join(location, "syscallLookup/scrapedi386.pickle"), "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[1]: k for k, v in scraped.items()}
    else:
        with open(os.path.join(location, "syscallLookup/scraped%s.pickle" % arch), "rb") as scrapeHandle:
            scraped = pickle.load(scrapeHandle)
        reverse = {v[0]: k for k, v in scraped.items()}
    
    syscalls = []
    key = startingsyscall
    reverseMax = max(scraped)

    for x in reverse:
        while key not in scraped and key < reverseMax:
            key += 1 # index might skip sometimes

        if string in x.lower():
            syscalls.append(_syscallLookup(key, arch, scraped))
        
        key += 1

    return syscalls

def syscalli386(query):
    if type(query) == str:
        return _reverseLookup(query, "i386")
    elif type(query) == int:
        return _syscallLookup(query, "i386")
    raise Exception("Invalid type: " + str(type(query)))

def syscallx86_64(query):
    if type(query) == str:
        return _reverseLookup(query, "x86_64")
    elif type(query) == int:
        return _syscallLookup(query, "x86_64")
    raise Exception("Invalid type: " + str(type(query)))

def syscallx86_32(query):
    if type(query) == str:
        return _reverseLookup(query, "x86_32", 0x40000000)
    elif type(query) == int:
        return _syscallLookup(query, "x86_32")
    raise Exception("Invalid type: " + str(type(query)))

def syscallArm64(query):
    if type(query) == str:
        return _reverseLookup(query, "arm64")
    elif type(query) == int:
        return _syscallLookup(query, "arm64")
    raise Exception("Invalid type: " + str(type(query)))

def syscallPowerPC(query):
    if type(query) == str:
        return _reverseLookup(query, "powerPC")
    elif type(query) == int:
        return _syscallLookup(query, "powerPC")
    raise Exception("Invalid type: " + str(type(query)))

def syscallMips64(query): #this is n64
    if type(query) == str:
        return _reverseLookup(query, "mips64", 5000)
    elif type(query) == int:
        return _syscallLookup(query, "mips64")
    raise Exception("Invalid type: " + str(type(query)))

def syscallMips32(query):
    if type(query) == str:
        return _reverseLookup(query, "mips32", 6000)
    elif type(query) == int:
        return _syscallLookup(query, "mips32")
    raise Exception("Invalid type: " + str(type(query)))

def syscallMipso32(query):
    if type(query) == str:
        return _reverseLookup(query, "mipso32", 4000)
    elif type(query) == int:
        return _syscallLookup(query, "mipso32")
    raise Exception("Invalid type: " + str(type(query)))

def syscallSparc64(query):
    if type(query) == str:
        return _reverseLookup(query, "sparc64")
    elif type(query) == int:
        return _syscallLookup(query, "sparc64")
    raise Exception("Invalid type: " + str(type(query)))

def syscallSparc32(query):
    if type(query) == str:
        return _reverseLookup(query, "sparc32")
    elif type(query) == int:
        return _syscallLookup(query, "sparc32")
    raise Exception("Invalid type: " + str(type(query)))

def syscallia64(query):
    if type(query) == str:
        return _reverseLookup(query, "ia64")
    elif type(query) == int:
        return _syscallLookup(query, "ia64")
    raise Exception("Invalid type: " + str(type(query)))

def sysprint(dicarr):
    if type(dicarr) == list:
        index = len(dicarr)
        for dic in dicarr:
            sysprint(dic)
            if index != 1:
                print("")
            index -= 1
        return
    for entry in dicarr:
        print(entry + ": " + str(dicarr[entry]))
