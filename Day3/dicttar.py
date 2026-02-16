def fkv(dict,target):
    lst=[]
    for key,value in dict.items():
        if value==target:
            lst.append(key)
    if not lst:
        print("Value not found")
    else:
        print("Keys for target is:", lst)
        
n=int(input("Enter the number elements: "))
data={}
for i in range(n):
    key=int(input("Enter key: "))
    value=input("Enter value: ")
    data[key]=value
target=input("Enter the value to find the key: ")
fkv(data,target)