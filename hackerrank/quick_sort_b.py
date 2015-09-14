#! /usr/bin/env python
import sys
import random
import time

# data = sys.stdin.readlines()
nums = random.sample(xrange(20), 10)

def q_sort(nums):
    if len(nums) > 0:
        pivot = nums[0]
        
        low = q_sort([x for x in nums[1:] if x < pivot])
        hi = q_sort([x for x in nums[1:] if x > pivot])
            
        return low + [pivot] + hi
    else:
        return []

start_time = time.time()
array = q_sort(nums)
end_time = time.time()
print array
print "Exec Time %.6f secs" % (float(end_time - start_time))