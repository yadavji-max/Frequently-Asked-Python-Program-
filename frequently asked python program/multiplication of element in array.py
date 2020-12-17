'''
a=[1,2,3,4]
m=1
for i in range(0,len(a)):
    m=m*a[i]
print(m)    
'''
#------------------------
import numpy
a=[1,2,3,4]
m=numpy.prod(a)
print(m)
