'''
a=[0,1,2,3,4,4,3,2,1]
max=a[0]
min=a[0]
l=len(a)

for i in range(1,l):
    if max<a[i]:
        max=a[i]
print("max element of array: " ,max)

for i in range(1,l):
    if min>a[i]:
        min=a[i]
print("min element of array: ", min)
'''
#------------------------------------
'''
a=[0,1,2,3,4,4,3,2,1]
l=len(a)
print(a)
a.sort() # small to bigger
print(a)
print("min element of array: ", a[0])
print("max element of array: ", a[l-1])
'''
#-------------------------------------

a=[0,1,2,3,4,4,3,2,1]
print("min element of array: ", min(a))
print("max element of array: ", max(a))








