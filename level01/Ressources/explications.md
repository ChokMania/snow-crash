On a acces au fichier /etc/passwd sur lequel on effectue un cat.
On peut observer dans le fichier que l'user flag01 a son mot de passe en visble mais chiffré.

<pre>
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
</pre>

On utilise donc l'outil de decryptage john the ripper avec les commandes suivantes :

<pre>
<code>> echo "flag01:42hDRfypTqqnw" > passwd</code>
<code>> john passwd</code>
<code>> john passwd --show</code>
</pre>


Ce qui nous donne :

<code>flag01:abcdefg</code>

On test le mot de passe :
<pre>
<code>> su flag01</code>
<code>Password: abcdefg</code>
</pre>

On obtient la phrase magique **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
</pre>
