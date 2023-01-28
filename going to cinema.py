"""
problem=1718B-GOing to Cinema
A company of n people is planning a visit to the cinema. Every person can either go to the cinema or not. That depends on how many other people will go. Specifically, every person i
said: "I want to go to the cinema if and only if at least ai other people will go, not counting myself". That means that person i will become sad if:
    1-they go to the cinema, and strictly less than ai other people go; or
    2-they don't go to the cinema, and at least ai other people go.
In how many ways can a set of people going to the cinema be chosen so that nobody becomes sad?

Input
Each test contains multiple test cases. The first line contains the number of test cases t(1≤t≤104). The description of the test cases follows.

Each test case consists of two lines. The first line contains a single integer n(2≤n≤2⋅105) — the number of people in the company.

The second line contains n integers a1,a2,…,an (0≤ai≤n−1) — integers from peoples' claims.
It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, print a single integer — the number of different ways to choose a set of people going to the cinema so that nobody becomes sad.
"""
#Solution
s=int(input())
while(s!=0):
    n=int(input())
    l=[int(i) for i in input().split()]
    l.sort()
    ans=0
    if(l[0]>0):
        ans=ans+1
    for i in range(0,n):
        if(i>=l[i]):
            l[i]='T'
        else:
            l[i]='F'
    
    for i in range(0,n):
        if(l[i]=='T'):
            if(i==0):
                ans=ans+1
            elif(l[i-1]=='F'):
                ans=ans+1
    print(ans)
    s=s-1