import sys
import random

nums = range(1, 6)
random.shuffle(nums)
print nums
# Step forward a position in the array for compare
for i in xrange(1, len(nums)):
    # Set index and capture element [6 |5| 7 1]
    j, v = i, nums[i]    
    # Compare elments (prev and curr) [|6| > |5| 7 1]
    while j > 0 and (nums[j-1] > v):
        # Swap elments (prev and curr) [|5| <-> |6| 7 1]
        nums[j] = nums[j-1]
        j -= 1
        
    nums[j] = v

print nums