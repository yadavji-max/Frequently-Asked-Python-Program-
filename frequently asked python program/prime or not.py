# natural num. > 1
# which has only 2 factor ( 1 and itself )
# exm.  19

# n=int(input("enter any num: "))
lst=[x for x in range(100)]
k=0
for n in lst:
    if n>=1:
        for i in range(1,n+1):
            if n%i == 0:
                k=k+1
        if k == 2:
            # print("prime")
            print(n)
        else:
            # print("not prime")
            pass
    else:
        # print("not natural")
        pass

 # another approach
 # 
 import math
lst=[]
n = int(input())
for i in range(n):
    lst.append(int(input()))

def isPrime(n):
    if n<=1:
        return False
    sqrt_n = math.sqrt(n)
    
    if isinstance(sqrt_n,int):
        return False
    
    for i in range(2,int(sqrt_n)+1):
        if n%i==0:
            return False
        
    return True    

for i in lst:
    if isPrime(i):
        print("Prime")
    else:
        print("Not prime")       
