def factorial(n):
    if n==0:
        result=1
    else:
        return n*factorial(n-1)
n=int(input("enter the number is"))
for i in range(1,n+1):
 print("the factorial of",i,"is",factorial(i))
    
