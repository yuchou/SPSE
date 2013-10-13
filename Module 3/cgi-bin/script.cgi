#!/usr/bin/perl
 
=head1 DESCRIPTION
 
printenv—demo CGI program which just prints its environment
 
=cut
print "Content-type: text/plain\r\n\r\n";
 
for my $var ( sort keys %ENV ) {
 my $value = $ENV{$var};
 $value =~ s/\n/\\n/g;
 $value =~ s/"/\\"/g;
 print qq[$var="$value"\n];
}
