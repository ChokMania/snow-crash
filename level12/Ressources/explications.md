https://unix.stackexchange.com/questions/86929/can-tr-work-with-regex
http://perl.mines-albi.fr/DocFr/perlrequick.html
https://regex101.com/


<pre><code>
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
	$nn = $_[1];
	$xx = $_[0];
	$xx =~ tr/a-z/A-Z/;
	$xx =~ s/\s.*//;
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
</code></pre>