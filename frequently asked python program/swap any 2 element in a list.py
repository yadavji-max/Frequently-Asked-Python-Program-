a=list(input("enter a list:"))
p1=int(input("enter pos-1 :"))
p2=int(input("enter pos-2 :"))
print(a)
a[p1-1],a[p2-1]=a[p2-1],a[p1-1]
print(a)

