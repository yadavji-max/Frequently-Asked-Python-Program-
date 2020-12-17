
a=[1,2,3,4,5]

"""
print(a)
a[0],a[-1]=a[-1],a[0]
print(a)

"""
#---------------
"""
print(a)
p=(a[0],a[-1])
a[-1],a[0]=p
print(a)

"""
#---------------
"""
print(a)
start,*middle,end=a
a=[end,*middle,start]
print(a)

"""
#---------------


print(a)
f=a.pop(0)
l=a.pop(-1)
a.insert(0,l)
a.append(f)
print(a)






