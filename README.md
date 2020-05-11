# syscallDB
## Syscall database
Have you ever been doing some assembly and finding yourself looking furiously for some nisch syscall\
Well, that will no longer be a problem with syscallDB's reverse lookup. It displays all relevant registers\
For the query that is given. The database currently supports x86, i386, arm64, powerpc and mips n64.\
More is to come. If you have any suggestion for additions or improvements, mail me at marwenn02@gmail.com 

## Usage
### x86
```py
$ python3
>>> import sysDB
>>> sysDB.syscall32("exec") # you do not need to know the whole name of the syscall.
[{'syscall': 'sys_execve', 'eax': 11, 'ebx': 'char __user *', 'ecx': 'char __user *__user *', 'edx': 'char __user *__user *', 'esi': 'struct pt_regs *', 'edi': ''}, {'syscall': 'sys_kexec_load', 'eax': 263, 'ebx': 'unsigned long entry', 'ecx': 'unsigned long nr_segments', 'edx': 'struct kexec_segment __user *segments', 'esi': 'unsigned long flags', 'edi': ''}]
```
### i386
```py
$ python3
>>> import sysDB
>>> sysDB.syscall64("execve")
[{'syscall': 'sys_execve', 'rax': 59, 'rdi': 'const char *filename', 'rsi': 'const char *const argv[]', 'rdx': 'const char *const envp[]'}, {'syscall': 'stub_execveat', 'rax': 322, 'rdi': 'int dfd', 'rsi': 'const char __user *filename', 'rdx': 'const char __user *const __user *argv', 'r10': 'const char __user *const __user *envp', 'r8': 'int flags'}]
```
### arm64
```py
$ python3
>>> import sysDB
>>> sysDB.syscallarm64("execve")
[{'syscall': 'execve', 'x8': '0xDD', 'x0': 'const char __user *filename', 'x1': 'const char __user *const __user *argv', 'x2': 'const char __user *const __user *envp', 'x3': '', 'x4': '', 'x5': ''}, {'syscall': 'execveat', 'x8': '0x119', 'x0': 'int dfd', 'x1': 'const char __user *filename', 'x2': 'const char __user *const __user *argv', 'x3': 'const char __user *const __user *envp', 'x4': 'int flags', 'x5': ''}]
```
### powerpc
```py
$ python3
>>> import sysDB
>>> sysDB.syscallPPC(4)
{'syscall': 'write', 'r0': 4, 'r3': 'unsigned int fd', 'r4': 'const char *buf', 'r5': 'size_t count', 'r6': '', 'r7': '', 'r8': ''}
```
### mips n64
```py
$ python3
>>> import sysDB
>>> sysDb.syscallMips64(5009)
{'syscall': 'sys_mmap', 'v0': 5009, 'a0': 'struct mmap_arg_struct', 'a1': '', 'a2': '', 'a3': '', 'a4': '', 'a5': ''}
```
## Installation
sysDB now also exists as a python package, install with
`python3 -m pip install sysDB`
For more regularly updated versions:
```sh
git clone https://github.com/marwenn02/syscallDB/
cd syscallDB/
./install.sh
```
