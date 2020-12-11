We have access to the file **/etc/passwd** on which we make a <code>cat</code>
We can see in the file that the user flag01 has his password visible but encrypted

<pre>
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
</pre>

So we use the decryption tool **john the ripper** with the following commands on an external terminal :

<pre>
<code>> echo "flag01:42hDRfypTqqnw" > passwd</code>
<code>> john passwd</code>
<code>> john passwd --show</code>
</pre>


Which gives us :

<code>flag01:abcdefg</code>

We test the password :
<pre>
<code>> su flag01</code>
<code>Password: abcdefg</code>
</pre>

You get the magic phrase **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
</pre>
