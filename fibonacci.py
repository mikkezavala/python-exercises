#! /usr/bin/env python
"""
# ------------------
# Fibonacci numbers
# ------------------
"""

import sys
import time

def fib(n):
    a, b, l = 1, 1, []
    for x in xrange(2, n):
        a, b = b, a + b
        
        l.append(b)
    
    print "Sequence: %s" % ", ".join(map(str, l))
    return b

start_time = time.time()

look = 11
print "Fib Number: %s of F(%s)" % (fib(look), look) 
end_time = time.time()

print "Exec Time %.10f secs" % (float(end_time - start_time))