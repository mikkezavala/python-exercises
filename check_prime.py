#! /usr/bin/env python
import sys
import random
import time


def is_prime(n):
    if n > 1:
        for i in xrange(2, int((n **0.5) + 1)):
            if n % i == 0:
                yield False            
        yield True
    yield False

start_time = time.time()

nums = []
for x in xrange(1000):
    if is_prime(x).next():
        pass # nums.append(x)
        
end_time = time.time()
print ",".join([str(x) for x in nums])
print "Exec Time %.3f secs" % (float(end_time - start_time))