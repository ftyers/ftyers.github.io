#!/usr/bin/perl

while ($line = <>) {
	$line =~ s/(\D+)\/(\D+)/\1 \/ \2/g;
	print $line;
}


