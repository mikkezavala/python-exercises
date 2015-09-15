#! /usr/bin/env python
import sys
import random
import time


def b_search(l, value):
    lo, hi = 0, len(l)-1
    
    while lo <= hi:
        mid = (lo + hi) / 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
            
    return -1


nums = random.sample(xrange(400000), 220000)

start_time = time.time()
print b_search(nums, 2)
end_time = time.time()

print "Exec Time %.3f secs" % (float(end_time - start_time))