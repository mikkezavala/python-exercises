#! /usr/bin/env python
import sys
import random
import time

# data = sys.stdin.readlines()
nums = random.sample(xrange(20), 10)

def m_sort(nums):
    if len(nums) <= 1:
        return nums
        
    out = []
    # drop remaining
    mid = len(nums) // 2
    
    left, right = m_sort(nums[:mid]), m_sort(nums[mid:])
    
    i, j = 0, 0
     
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
            
    while i < len(left):
        out.append(left[i])
        i += 1
        
    while j < len(right):
        out.append(right[j])
        j += 1
        
    return out

start_time = time.time()
array = m_sort(nums)
end_time = time.time()
print array
print "Exec Time %.6f secs" % (float(end_time - start_time))