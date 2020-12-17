a=[1,2,3,4,5]
e=6
'''

f=0
for i in range(0,len(a)):
    if a[i]==e:
        print("element present")
        f=f+1
        break
if f==0:
    print("element not present")
    
'''

#---------------------------------

if e not in a:
    print("element not present")
else:
    print("element  present")

