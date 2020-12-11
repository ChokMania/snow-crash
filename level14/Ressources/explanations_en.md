We find rine in the **home** folder this time, and we have nothing more than for the other levels. So we understand that we will have to exploit **getflag**

We want to know what the binary does, so we use **ltrace** :
<pre><code>> ltrace /bin/getflag
__libc_start_main(0x8048946, 1, 0xbffff7e4, 0x8048ed0, 0x8048f40 <unfinished ...>
ptrace(0, 0, 1, 0, 0)= -1
puts("You should not reverse this"You should not reverse this)= 28
+++ exited (status 1) +++
</code></pre>
> **ptrace** provides the parent process with a way to control the execution of another process

And we analyze the binary itself :
```
> gdb -q /bin/getflag
Reading symbols from /bin/getflag...(no debugging symbols found)...done.
(gdb) > disas main
Dump of assembler code for function main:
...
   0x08048989 <+67>:    call   0x8048540 <ptrace@plt>
...
   0x08048afd <+439>:   call   0x80484b0 <getuid@plt>
...
End of assembler dump.
```
We find a resemblance with the previous level except that **ptrace** will block our attempts to modify the value of **getuid**
The goal here will be to take the uid of flag14 which is in :
<pre><code>> cat /etc/passwd | grep flag14
flag14:x:3014:3014::/home/flag/flag14:/bin/bash

> id flag14
uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)
</code></pre>
> So 3014

We will therefore create a .gdb file containing the following instructions, with instructions for bypass **ptrace** :
<pre>file /bin/getflag	# Take as a basis the binary  getflag
catch syscall ptrace 	# Creation of a catch point for ptrace
commands 1
set $eax=0		# Change in the value of its return
continue		# Continue after
end
break getuid		# Create a breakpoint a get uid
run			# Launch the debug
step			# Advance to breakpoint
print $eax		# Display %eax
set $eax=3014		# Change its value for 3014
print $eax		# Display %eax
step			# Goes to the end of the program
</pre>
> <pre><code>printf "file /bin/getflag\ncatch syscall ptrace\ncommands 1\nset (\$eax) = 0\ncontinue\nend\nbreak getuid\nrun\nstep\nprint \$eax\nset \$eax=3014\nprint \$eax\nstep\n" > /tmp/file.gdb</code></pre>

The only thing left to do is to throw it :

<pre><code>> gdb -x /tmp/file.gdb -q -batch
Catchpoint 1 (syscall 'ptrace' [26])
Breakpoint 2 at 0x80484b0

Catchpoint 1 (call to syscall ptrace), 0xb7fdd428 in __kernel_vsyscall ()

Catchpoint 1 (returned from syscall ptrace), 0xb7fdd428 in __kernel_vsyscall ()

Breakpoint 2, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
Single stepping until exit from function getuid,
which has no line number information.
0x08048b02 in main ()
$1 = 2014
$2 = 3014
Single stepping until exit from function main,
which has no line number information.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6
</code></pre>