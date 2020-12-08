On trouve dans le dossier home un file token et un binaire **./level13** qui, si on le lance nous affiche un message:
<pre><code>> ./level13
UID 2013 started us but we we expect 4242
</code></pre>

On va donc chercher a changer l'uid, ou plutot la valeur de l'uid dans le binaire.
Pour cela nous allons utiliser GNU Debugeur (gdb)

On commence par analyser le binaire en lui même:
```
> gdb -q level13
Reading symbols from /home/user/level13/level13...(no debugging symbols found)...done.
(gdb) > disas main
Dump of assembler code for function main:
   0x0804858c <+0>:     push   %ebp						# Mettre registre %ebp en tête de stack
   0x0804858d <+1>:     mov    %esp,%ebp				# Pour le debugging
   0x0804858f <+3>:     and    $0xfffffff0,%esp			# Allignement de stack
   0x08048592 <+6>:     sub    $0x10,%esp				# Alligement de stack
   0x08048595 <+9>:     call   0x8048380 <getuid@plt>	# Call getuid, stock dans %eax
   0x0804859a <+14>:    cmp    $0x1092,%eax				# Comparaison entre 0x1092 (4242) et %eax
   0x0804859f <+19>:    je     0x80485cb <main+63>		# Si comparaison bonne jump main+63
   0x080485a1 <+21>:    call   0x8048380 <getuid@plt>
   0x080485a6 <+26>:    mov    $0x80486c8,%edx
   0x080485ab <+31>:    movl   $0x1092,0x8(%esp)
   0x080485b3 <+39>:    mov    %eax,0x4(%esp)
   0x080485b7 <+43>:    mov    %edx,(%esp)
   0x080485ba <+46>:    call   0x8048360 <printf@plt>
   0x080485bf <+51>:    movl   $0x1,(%esp)
   0x080485c6 <+58>:    call   0x80483a0 <exit@plt>
   0x080485cb <+63>:    movl   $0x80486ef,(%esp)		# Stock 0x80486ef (134514415) dans %esp
   0x080485d2 <+70>:    call   0x8048474 <ft_des>		# Call ft_des
   0x080485d7 <+75>:    mov    $0x8048709,%edx			# Charge 0x8048709 (134514441) dans %edx
   0x080485dc <+80>:    mov    %eax,0x4(%esp)			# Stock %eax 4 bits au dessus de %esp
   0x080485e0 <+84>:    mov    %edx,(%esp)				# Stock %edx, dans %esp
   0x080485e3 <+87>:    call   0x8048360 <printf@plt>		# Call printf
   0x080485e8 <+92>:    leave							# Clean %ebp
   0x080485e9 <+93>:    ret								# Fin de fonction
End of assembler dump.
```

> On remarque que la commande getuid est faite est stock son resultat dans **%eax** et fait une comparaison juste derriere avec **0x1092 (4242)** ce qui estce que l'on cherche.

On va creer un fichier .gdb contenant les instructions suivantes:
<pre>file /home/user/level13/level13	# Prendre pour base le binaire level13
break getuid			# Creer un breakpoint a get uid
run				# Lance le debug
step				# Avance vers le breakpoint
print $eax			# Affiche %eax
set $eax=4242			# Change sa valeur pour 4242
print $eax			# Affiche %eax
step				# Avance jusqu'a la fin du programme
</pre>
> <pre><code>printf "file /home/user/level13/level13\nbreak getuid\nrun\nstep\nprint \$eax\nset \$eax=4242\nprint \$eax\nstep\n" > /tmp/file.gdb</code></pre>

Il ne reste plus qu'a le lancer:

<pre><code>> gdb -x /tmp/file.gdb -q -batch
Breakpoint 1 at 0x8048380

Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
Single stepping until exit from function getuid,
which has no line number information.
0x0804859a in main ()
$1 = 2013
$2 = 4242
Single stepping until exit from function main,
which has no line number information.
your token is 2A31L79asukciNyi8uppkEuSx
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6
</code></pre>
