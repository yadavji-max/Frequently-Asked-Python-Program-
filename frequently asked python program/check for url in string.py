import re

str="you can google at http://www.google.com/"

# http://urlregex.com/

a=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
print(a)
