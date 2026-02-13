def sq(lst):
    sqlst=[i*i for i in lst if i%2==0]
    return sqlst

n=int(input("Enter the number of elements: "))
lst=[]
for i in range(n):
    num=int(input("Enter a number: "))
    lst.append(num)
print(sq(lst))