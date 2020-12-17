a="i am saurabh"
b="i am s@urabh"

import re

regex=re.compile('[@_!#$%*()<>?/\|}{~:]')
if(regex.search(b)==None):
    print("not present")
else:
    print("present")
    


                 
