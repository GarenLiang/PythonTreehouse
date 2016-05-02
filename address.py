# PythonTreehouse
import re
line=re.search(r'''
        ^(?P<name>[-\w ]*,\s[-\w ]+)\t #Last and first name
        (?P<Email>[-\w\d.+]+@[-\w\d.]+)\t  #Email
        (?P<Phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  #Phone
        (?P<Job>[\w\s]+,\s[\w\s.]+)\t?  #Job and company
        (?P<Twitter>@[\w\d]+)?$   #Twitter
''',data,re.X|re.M)
print(line)
print(line.groupdict())
