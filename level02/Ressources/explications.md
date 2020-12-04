On trouve dans le dossier home un fichier **level02.pcap**

On sait que ces fichiers contiennent le log d'un trafic reseau

On cherche a le recuperer pour pouvoir l'analyser, ainsi on utlise la commande suivante:

<pre><code> sudo scp -P4242 -r level02@IP:/home/user/level02/level02.pcap </code></pre>

On essaye de lire le conenu du fichier .pcap avec la commande :

<pre><code>tcpick -C -yU -r level02.pcap</code></pre>

Qui nous donne (la partie intéressante):
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

> On sait que le 7f correspond au code ASCII DEL

Donc ft_wandr<7f><7f><7f>NDRel<7f>L0L donne donc:

<code>ft_wa~~ndr~~NDRe~~l~~L0L -> ft_waNDReL0L</code>


On test le mot de passe :
<pre>
<code>> su flag02</code>
<code>Password: ft_waNDReL0L</code>
</pre>

On obtient la phrase magique **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
</pre>

