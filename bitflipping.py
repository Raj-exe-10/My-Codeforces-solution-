#Bit Flipping

'''
Problem

Given an integer A.
Write binary representation of the integer without leading zeros.
Flip all bits then return the integer value of the binary number formed.
Flipping means 0 -> 1 and 1 -> 0.
'''

#solution

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        a1=str(bin(A))
        a2=''
        for i in range (2,len(a1)):
            if int(a1[i])==0:
                a2+='1'
            else:
                a2+='0'
        return int(a2,2)