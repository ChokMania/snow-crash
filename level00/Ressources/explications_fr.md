On cherche à savoir à quels fichiers nous avons accès, donc on utilise la commande :

<pre>
<code>> find / -user flag00 -print 2>/dev/null</code>
<code>/usr/sbin/john
/rofs/usr/sbin/john</code>
</pre>

Le contenu des deux fichiers est exactement le même:

<code>cdiiddwpgswtgt</code>

On cherche donc à déchiffrer ce dernier.
On se rend compte qu'il s'agit d'un **ROT**, plus précisément un **ROT-15** qui nous donne :

<code>nottoohardhere</code>

On teste le mot de passe :
<pre>
<code>> su flag00</code>
<code>Password: nottoohardhere</code>
</pre>

On obtient la phrase magique **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
</pre>

