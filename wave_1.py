#Wave Array

'''
Problem Description
 

Given an array of integers A, sort the array into a wave-like array and return it. 
In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5..... 
NOTE: If multiple answers are possible, return the lexicographically smallest one.



Problem Constraints
1 <= len(A) <= 106
'''

#solution

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
            l1=A
            l1.sort()
            if len(l1)%2==0:
                for i in range(0,len(l1),2):
                    l1[i],l1[i+1]=l1[i+1],l1[i]
            return l1
            