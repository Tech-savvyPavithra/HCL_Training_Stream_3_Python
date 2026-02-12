def multiplication_table(n, e):
    for i in range(1,e+1):
        print(n,"x",i,"=",n*i) 

print("Enter the num for multiplication table:")
n=int(input())
print("Enter the times the table should end:")
e=int(input())
print("Multiplication table of",n,"is:")
 
multiplication_table(n,e)