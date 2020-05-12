# syscallDB
## Syscall database
Have you ever been doing some assembly and finding yourself looking furiously for some nisch syscall\
Well, that will no longer be a problem with syscallDB's reverse lookup. It displays all relevant registers\
For the query that is given. The database currently supports x86, i386, arm64, powerpc and mips n64.\
More is to come. If you have any suggestion for additions or improvements, mail me at marwenn02@gmail.com 
## Installation
sysDB now also exists as a python package, install with
`python3 -m pip install sysDB`
For more regularly updated versions:
```sh
git clone https://github.com/marwenn02/syscallDB/
cd syscallDB/
./install.sh
```
## Usage
### x86
```py
$ python3
>>> import sysDB
>>> sysDB.syscalli386("exec") # you do not need to know the whole name of the syscall.
[{'syscall': 'sys_execve', 'eax': 11, 'ebx': 'char __user *', 'ecx': 'char __user *__user *', 'edx': 'char __user *__user *', 'esi': 'struct pt_regs *', 'edi': ''}, {'syscall': 'sys_kexec_load', 'eax': 263, 'ebx': 'unsigned long entry', 'ecx': 'unsigned long nr_segments', 'edx': 'struct kexec_segment __user *segments', 'esi': 'unsigned long flags', 'edi': ''}]
```
### i386
```py
$ python3
>>> import sysDB
>>> sysDB.syscallx86("execve")
[{'syscall': 'sys_execve', 'rax': 59, 'rdi': 'const char *filename', 'rsi': 'const char *const argv[]', 'rdx': 'const char *const envp[]'}, {'syscall': 'stub_execveat', 'rax': 322, 'rdi': 'int dfd', 'rsi': 'const char __user *filename', 'rdx': 'const char __user *const __user *argv', 'r10': 'const char __user *const __user *envp', 'r8': 'int flags'}]
```
### arm64
```py
$ python3
>>> import sysDB
>>> sysDB.syscallArm64("execve")
[{'syscall': 'execve', 'x8': '0xDD', 'x0': 'const char __user *filename', 'x1': 'const char __user *const __user *argv', 'x2': 'const char __user *const __user *envp', 'x3': '', 'x4': '', 'x5': ''}, {'syscall': 'execveat', 'x8': '0x119', 'x0': 'int dfd', 'x1': 'const char __user *filename', 'x2': 'const char __user *const __user *argv', 'x3': 'const char __user *const __user *envp', 'x4': 'int flags', 'x5': ''}]
```
### powerpc
```py
$ python3
>>> import sysDB
>>> sysDB.sysprint(sysDB.syscallPowerPC(4))
sc: sys_write
r0: 4
r3: unsigned int fd
r4: const char *buf
r5: size_t count
r6: 
r7: 
r8:
```
### mips64
```py
$ python3
>>> import sysDB
>>> sysDb.syscallMips64(5009)
{'syscall': 'sys_mmap', 'v0': 5009, 'a0': 'struct mmap_arg_struct', 'a1': '', 'a2': '', 'a3': '', 'a4': '', 'a5': ''}
```
### mips n32
```py
$ python3
>>> import sysDB
>>> sysDB.syscallMips32(6002)
{'syscall': 'sys_open', 'v0': 6002, 'a0': 'const char *filename', 'a1': 'int flags', 'a2': 'umode_t mode', 'a3': '', 'a4': '', 'a5': ''}
```
### mips o32
```py
$ python3
>>> import sysDB
>>> sysDB.syscallMipso32(4005)
{'syscall': 'sys_open', 'v0': 4005, 'a0': 'const char *filename', 'a1': 'int flags', 'a2': 'umode_t mode', 'a3': '', 'stack1': '', 'stack2': ''}
```
### sparc64
```py
$ python3
>>> import sysDB
>>> sysDB.syscallSparc64(0)
{'t 0x6d': 'sys_restart_syscall', 'g1': 0, 'o0': '', 'o1': '', 'o2': '', 'o3': '', 'o4': '', 'o5': ''}
```
### sparc32
```py
$ python3
>>> import sysDB
>>> sysDB.syscallSparc32(0)
{'t 0x10': 'sys_restart_syscall', 'g1': 0, 'o0': '', 'o1': '', 'o2': '', 'o3': '', 'o4': '', 'o5': ''}
```
