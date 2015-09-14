#! /usr/bin/env python
import sys

a, b, c = [0,1,5]
# Tn+2 = (Tn+1)2 + Tn
def mod_fibo(a, b, c):
    # first two terms already there
    if c > 2:
        # third and ahead (n)
        for i in xrange(2, c):
            # "a" gets "b" and compute "n"
            a, b = b, (b * b) + a           
        return b
    return b if c == 2 else a
    
print mod_fibo(a,b,c)