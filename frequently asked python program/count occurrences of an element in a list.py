'''
a=[1,2,3,4,5,6,3,2,3,2,2,3]
x=1
print("{} has occured {} times".format(x,a.count(x)))
'''
#-------------------
from collections import Counter
a=[1,2,3,4,5,6,3,2,3,2,2,3]
x=1
d=Counter(a)
print(d)
print("{} has repeted {} times".format(x,d[x]))
