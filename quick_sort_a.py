#! /usr/bin/env python
import sys
import random
import time

# data = sys.stdin.readlines()
nums = random.sample(xrange(10000), 10000)

def q_sort(nums, left, right):
    i, j = left, right
    pivot = int(nums[i] + nums[j]) / 2
    
    while i < j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
         
        if i <= j:
            x = nums[j]
            nums[j] = nums[i]
            nums[i] = x
            
            i +=1
            j -=1
            
    
    if left < j:
        nums = q_sort(nums, left, j)
    if right > i:
        nums = q_sort(nums, i, right)
        
    return nums

start_time = time.time()
array = q_sort(nums, 0, (len(nums) - 1))
end_time = time.time()
print array
print "Exec Time %.6f secs" % (float(end_time - start_time))