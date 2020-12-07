On trouve dans le dossier home un file token et un binaire ./level09 qui, si on le lance nous affiche un message:
<pre><code>> ./level09
You need to provied only one arg.
> ./level09 token
tpmhr
> level09@SnowCrash:~$ ./level09 abcdefg
acegikm
> level09@SnowCrash:~$ ./level09 aaaaaaa
abcdefg
</code></pre>

Apres quelques essais, on comprend que le binaire a servi a encoder le fichier **token**.
Pour chaque char, on ajoute à sa valeur ASCII, sa position dans la string.

On cherche donc a faire un programme qui va decrypter le contenu de token,
ainsi on télécharge token pour pouvoir travailler avec:
<pre><code>sudo scp -P4242 -r level09@192.168.1.42:/home/user/level09/token .</code></pre>

Grace au code ci dessous, nous pouvons decrypter le contenu de token:
```python
# coding: utf-8
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("str", help="file to decrypt")
	args = parser.parse_args()
	args.str = args.str.encode("utf-8", "surrogateescape")
	for i in range(len(args.str)):
		print(chr(args.str[i] - i), end="")
	print()
```
<pre><code>> python3 decrypt.py `cat token`
f3iji1ju5yuevaus41q1afiuq
</code></pre>

On test le mot de passe :
<pre>
<code>> su flag08</code>
<code>Password: f3iji1ju5yuevaus41q1afiuq</code>
</pre>

On obtient la phrase magique **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
</pre>