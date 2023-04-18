#Maximum Substring
'''
problem
Given a string A consisting of only characters 'a' and 'b'.
Divide the string into substrings of length B.
Find the subtring with maximum count of 'a' and return the count.

Note: If the length of the string is not a multiple of B and there are some characters left in the end consider them also as a substring.
'''
#solution

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max1=0
        cnt=0
        for i in range(len(A)):
            if i%B==0:
                max1 = max(max1,cnt)
                cnt=0
            if A[i]=='a':
                cnt+=1
        return max(max1,cnt)   