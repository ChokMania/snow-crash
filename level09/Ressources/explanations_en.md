We find in the **home** folder a **token** file and a **level09** binary which, if we launch it, displays a :
<pre><code>> ./level09
You need to provied only one arg.
> ./level09 token
tpmhr
> level09@SnowCrash:~$ ./level09 abcdefg
acegikm
> level09@SnowCrash:~$ ./level09 aaaaaaa
abcdefg
</code></pre>

After a few tries, we understand that the binary was used to encode the **token** file.
For each char, its position in the string is added to its ASCII value

We find in the **home** folder a **token** file and a **level09** binary which, if we launch it, displays a :
so we download **token** to be able to work with :
<pre><code>sudo scp -P4242 -r level09@IP:/home/user/level09/token .</code></pre>

Thanks to the code below, we can decrypt the content of the token :
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

We test the password :
<pre>
<code>> su flag09</code>
<code>Password: f3iji1ju5yuevaus41q1afiuq</code>
</pre>

You get the magic phrase **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
</pre>