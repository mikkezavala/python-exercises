#! /usr/bin/env python
"""
# --------------------
# Multiples of 3 and 5
# --------------------
#
# If we list all the natural numbers below 10 that are multiples of 
# 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

"""
import sys
import time

start_time = time.time()
out = 0
for i in xrange(1000):    
    if (i % 3 == 0) or (i % 5 == 0):
        out += i

print out
end_time = time.time()
print "Exec Time %.3f secs" % (float(end_time - start_time))