import re
date="2025-11-30" #YYYY-MM-DD
pattern = r"^\d{4}-\d{2}-\d{2}$"
#more = r"^\d{4}-(0[1-9]|1[0-2])-\d{2}$" month range also checking here
if re.match(pattern, date):
    print("Date is valid")
else:
    print("Date is invalid")