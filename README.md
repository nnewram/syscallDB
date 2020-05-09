# syscallDB
## x86 and x64 syscall database
Have you ever been doing some assembly and finding yourself looking furiously for some nisch syscall
Well, that will no longer be a problem with syscallDB's reverse lookup, did you forget rax for execve?
```py
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
