"""
Bhavneet Singh ,GeeksForGeeks 
Originally using C++
"""

import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)
#print(sys.getrecursionlimit())

dp = [-1]*1000000

def fib(n):
    if(n<=1):
        return n
    
    if (dp[n - 1] != -1) :
        first = dp[n - 1]
    else:
        first = fib(n - 1)
  
    if (dp[n - 2] != -1) :
        second = dp[n - 2] 
    else:
        second = fib(n - 2)

    dp[n] = first+second
    #print(dp[n])
    return dp[n]

n = int(input("Enter the n value: "))
print("Nth term is : ",fib(n))