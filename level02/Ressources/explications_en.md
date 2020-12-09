We find in the home folder a file **level02.pcap**

We know that these files contain the log of a network traffic

We try to retrieve it to be able to analyze it, so we use the following command on an external terminal :

<pre><code>> sudo scp -P4242 -r level02@IP:/home/user/level02/level02.pcap .</code></pre>

We try to read the contents of the **.pcap** file with the command :

<pre><code>> tcpick -C -yU -r level02.pcap</code></pre>

Who gives us (the interesting part) :
<pre>
Linux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)

<01><00>wwwbugs login:
l
<00>l
e
<00>e
v
<00>v
e
<00>e
l
<00>l
X
<00>X

<01>
<00>
Password:
f
t
_
w
a
n
d
r
<7f>
<7f>
<7f>
N
D
R
e
l
<7f>
L
0
L

<00>
<01>
<00>
</pre>

> We know that 7f corresponds to the ASCII code "DEL"

So ft_wandr<7f><7f><7f>NDRel<7f>L0L gives :

<code>ft_wa~~ndr~~NDRe~~l~~L0L -> ft_waNDReL0L</code>


We test the password :
<pre>
<code>> su flag02</code>
<code>Password: ft_waNDReL0L</code>
</pre>

You get the magic phrase **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
</pre>

