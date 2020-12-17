#a=['saurabh','suman','kritika','kashiah','saurabh','karishma','saurabh','shikha']
#a=['saurabh', 'suman', 'kritika', 'kashiah', 'saurabh']
a=[1,2,3,4,5,1,2,1]



c=0
e=2
#n='saurabh'
n=1

print(a)

for i in range(0,len(a)):
    if a[i]==n:
        c=c+1
        if c==e:
            del a[i]
            break
print(a)
