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
rdi: const char *filename
rsi: const char *const argv[]
rdx: const char *const envp[]

syscall: stub_execveatint
rax: 322
rdi: int dfd
rsi: const char __user *filename
rdx: const char __user *const __user *argv
r10: const char __user *const __user *envp
r8: int flags
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
## pip
sysDB now also exists as a python package, install with
`python3 -m pip install sysDB`
### Usage
```
>>> import sysDB
>>> sysDB.syscall64("sys_write")
[{'syscall': 'sys_write', 'rax': 1, 'rdi': 'unsigned int fd', 'rsi': 'const char *buf', 'rdx': 'size_t count'}, {'syscall': 'sys_writev', 'rax': 20, 'rdi': 'unsigned long fd', 'rsi': 'const struct iovec *vec', 'rdx': 'unsigned long vlen'}]
>>> sysDB.syscall32("execve")
[{'syscall': 'sys_execve', 'eax': 11, 'ebx': 'char __user *', 'ecx': 'char __user *__user *', 'edx': 'char __user *__user *', 'esi': 'struct pt_regs *', 'edi': ''}]
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
