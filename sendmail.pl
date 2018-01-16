#!/usr/bin/perl
#
# send email using the vmaxx.tech smtp server
#
# code by Jinjun Wang
# 2016 12 22
#

use warnings;
use strict;

use Data::Dumper;
use Net::SMTP;

my ($mailto, $subject, $text) = @ARGV;

##########################################
# parameters
my $mailhost = "smtp.ym.163.com"; # the smtp host
my $mailfrom = 'VMaxx AI Robot<robot@vmaxx.tech>'; # your email address

my $acc = 'robot@vmaxx.tech';
my $pwd = 'Xjtu123456';

##########################################
#
print "333";
my $smtp = Net::SMTP->new($mailhost, Hello => 'localhost', Timeout => 120) or die "Cannot connect to server $!";

print "1111Hello, world\n";
#print "$!";
print "lll";
print "33333";
# anth login, type your user name and password here
$smtp->auth($acc, $pwd) or die "Could not authenticate $!";
print "2233";

# Send the From and Recipient for the mail servers that require it
$smtp->mail($mailfrom);
$smtp->to($mailto);

# Start the mail
$smtp->data();

# Send the header
$smtp->datasend("MIME-Version: 1.0\n");
$smtp->datasend("Content-Type: text/html; charset=UTF-8 \n");
$smtp->datasend("To: $mailto\n");
$smtp->datasend("From: $mailfrom\n");
$smtp->datasend("Subject: $subject\n");
$smtp->datasend("\n");

# Send the message
$text .= "<br />This is a system generated message, so please don't reply. Visit <a href='http://www.vmaxx.co'>www.vmaxx.co</a> for more information.<br/>";


$smtp->datasend("$text\n\n");

# Send the termination string
$smtp->dataend();

$smtp->quit;

