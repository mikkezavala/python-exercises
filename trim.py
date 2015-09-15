#! /usr/bin/env python
import sys
import random
import time


def trim(s):
    if s[0] == ' ':
        s = s[1:]
    if s[-1] == ' ':
        s = s[:-1]
    
    if s[0] == ' ' or s[-1] == ' ':
        return trim(s)
    return s

string = "      Mikke    "
start_time = time.time()
string = trim(string)
end_time = time.time()
print "Trimmed '%s' Lenght: %s" % (string, str(len(string)))

print "Exec Time %.3f secs" % (float(end_time - start_time))