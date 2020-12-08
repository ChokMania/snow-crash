We want to know which files we have access to, so we use the command :

<pre>
<code>> find / -user flag00 -print 2>/dev/null</code>
<code>/usr/sbin/john
/rofs/usr/sbin/john</code>
</pre>

The content of both files is exactly the same:

<code>cdiiddwpgswtgt</code>

So we try to decipher it.
We realize that it is a **ROT**, more precisely a **ROT-15** which gives us :

<code>nottoohardhere</code>

We test the password:
<pre>
<code>> su flag00</code>
<code>Password: nottoohardhere</code>
</pre>

We get the magic phrase **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
</pre>
