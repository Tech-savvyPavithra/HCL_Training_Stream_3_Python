import re
email="221401058@rajalakshmi.edu.in, pavi05@gmail.com, helina@yahoo.com, info@company.co.uk"
pattern =re.findall(r"@([\w\.]+)",email)
print(pattern)

