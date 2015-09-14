#! /usr/bin/env python
""""
# About the Challenges 
# ---------------------
# The challenges will describe some topic and then ask you to code 
# a solution. As you progress through the challenges, you will learn
# some important concepts in algorithms. In each challenge, you will 
# receive input on STDIN and you will need to print the correct
# output to STDOUT.

# For many challenges, helper methods (like an array) will be 
# provided for you to process the input into a useful format. 
# You can use these methods to get started with your program, 
# or you can write your own input methods if you want. 
# Your code just needs to print the right output to each test case.

# Sample Challenge 
# -----------------
# This is a simple challenge to get things started. Given a sorted
# array (ar) and a number (V), can you print the index location of 
# V in the array?
"""
import sys

data = sys.stdin.readlines()

haystack = int(data[0])
dimension = int(data[1])
nums = [int(x) for x in data[2].split()]

# range takes from 0...(n-1)
for i in xrange(dimension):
    if haystack == nums[i]:
        print i