On ne trouve rine dans le dossier **home** cette fois ci, et nous n'avons rien de plus que pour les autres levels. On comprend donc que l'on va devoir exploiter **getflag**.

On cherche à savoir ce que le binaire fait, pour cela on utilise **ltrace**:
<pre><code>> ltrace /bin/getflag
__libc_start_main(0x8048946, 1, 0xbffff7e4, 0x8048ed0, 0x8048f40 <unfinished ...>
ptrace(0, 0, 1, 0, 0)= -1
puts("You should not reverse this"You should not reverse this)= 28
+++ exited (status 1) +++
</code></pre>
> ptrace fournit au processus parent un moyen de contrôler l'exécution d'un autre processus

Et on analyse le binaire en lui même:
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
On trouve une ressemblance avec le level précédent mis à part que **ptrace** va bloquer nos tentatives de modification de value de getuid.
Le but ici va être de prendre l'uid de flag14 qui se trouve dans :
<pre><code>> cat /etc/passwd | grep flag14
flag14:x:3014:3014::/home/flag/flag14:/bin/bash

> id flag14
uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)
</code></pre>
> Donc 3014

On va donc créer un fichier .gdb contenant les instructions suivantes, avec des instructions pour bypass **ptrace** :
<pre>file /bin/getflag	# Prendre pour base le binaire getflag
catch syscall ptrace 	# Creation d'un catch point pour ptrace
commands 1
set $eax=0		# Changement de valeur de son return
continue		# Continue apres
end
break getuid		# Creer un breakpoint a get uid
run			# Lance le debug
step			# Avance vers le breakpoint
print $eax		# Affiche %eax
set $eax=3014		# Change sa valeur pour 3014
print $eax		# Affiche %eax
step			# Avance jusqu'a la fin du programme
</pre>
> <pre><code>printf "file /bin/getflag\ncatch syscall ptrace\ncommands 1\nset (\$eax) = 0\ncontinue\nend\nbreak getuid\nrun\nstep\nprint \$eax\nset \$eax=3014\nprint \$eax\nstep\n" > /tmp/file.gdb</code></pre>

Il ne reste plus qu'a le lancer:

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