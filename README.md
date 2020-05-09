# syscallDB
## x86 and x64 syscall database
Have you ever been doing some assembly and finding yourself looking furiously for some nisch syscall\
Well, that will no longer be a problem with syscallDB's reverse lookup, did you forget rax for execve?
## x86
```sh
python3 syscallLookup.py -r
Syscall: execve

syscall: sys_execveconst
rax: 59
rdi: char
rsi: *filenameconst
rdx: char
r10: *const
r8: argv[]const
r9: char

syscall: stub_execveatint
rax: 322
rdi: dfdconst
rsi: char
rdx: __user
r10: *filenameconst
r8: char
r9: __user
```
## x64
```sh
python3 syscallLookup.py -32 -r
Syscall: exec

syscall: sys_execve
eax: 11
ebx: char __user *
ecx: char __user *__user *
edx: char __user *__user *
esi: struct pt_regs *
edi: 

syscall: sys_kexec_load
eax: 263
ebx: unsigned long entry
ecx: unsigned long nr_segments
edx: struct kexec_segment __user *segments
esi: unsigned long flags
edi:
```

## Installation
```sh
git clone https://github.com/marwenn02/syscallDB/
echo "this part is optional, but pickles should not be trusted."
cd syscallDB/syscallLookup/scrape
python3 syscallScrapex64.py
python3 syscallScrapex86.py
cd ..
```
