'''
n=int(input("enter a number: "))
f=1

if n==0:
    print("zero has factorial 1")
elif n<0:
    print("not possible for -ve number")
else:
    for i in range(1,n+1):
        f=f*i
    print("factorial of",n,"is",f)    

'''
#--------------------------------

n=int(input("enter a number: "))

def math(n):
    if n==0 or n==1:
        return 1
    else:
        return n*math(n-1)
        
print("factorial of",n,"is",math(n))
