#! /usr/bin/env python
import sys
import time


def panagram(s):
    if len(set([x.lower() for x in s if x != ' '])) == 26:
        return True
    return False

start_time = time.time()
word = "Jackdaws love my big sphinx of quartz "
print "Is Word '%s' a Panagram: %s" % (word, panagram(word))
end_time = time.time()
print "Exec Time %.3f secs" % (float(end_time - start_time))