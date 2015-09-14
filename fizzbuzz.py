#! /usr/bin/env python
import sys
import random
import time

start_time = time.time()
for i in xrange(101):
    out = ""
    if (i % 15 == 0):
        out += "FizzBuzz"  
    elif (i % 3 == 0):
        out += "Fizz"
    elif (i % 5 == 0):
        out = "Buzz"
    else:
        out = str(i)
        
    print out
end_time = time.time()
print "Exec Time %.3f secs" % (float(end_time - start_time))