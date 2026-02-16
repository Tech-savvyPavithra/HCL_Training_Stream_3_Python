def sal(data):
    maxx=max(data.values())
    out = [name for name, salary in data.items() if salary == maxx]
    return ", ".join(out)
n=int(input("Enter no  of employees: "))
data={}
for i in range(n):
   key=input("Enter employee name: ") 
   value = int(input("Enter the salary: "))
   data[key]=value
   
print(sal(data))
