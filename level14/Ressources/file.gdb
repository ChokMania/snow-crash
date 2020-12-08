file /bin/getflag
catch syscall ptrace
commands 1
set $eax=0
continue
end
break getuid
run
step
print $eax
set $eax=3014
print $eax
step