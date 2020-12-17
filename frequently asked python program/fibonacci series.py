# febonacci series
# 0 1 1 2 3 5 8 13
# i.e. sum of last two number


n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
l =int(input("enter iteration : "))
print(n1)
print(n2)

for i in range(2,l):
    sum=n1+n2
    print(sum)
    n1,n2=n2,sum


