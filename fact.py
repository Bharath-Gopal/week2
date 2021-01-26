import sys
sys.setrecursionlimit(15000)

def fact(n):
    if (n==1):
        return n
    else:
        return(n*fact(n-1))

n=int(input("enter a number: "))
print(fact(n))