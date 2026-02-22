from Package1.sub_package1 import calculator as c

print("Add:", c.add(10,20))
print("Sub:", c.sub(10,20))
print("Mul:", c.mul(10,20))
print("Div:", c.div(10,20))


import random as r

print("Random:", r.random()) #random float between 0 and 1
print("Random integer:", r.randint(1,6)) #limited to 1 to 6
print("Random choice:", r.choice(["Apple", "Banana", "Cherry", "Mango" , "Peach"])) #randomly select one item from the list
list1 = [1,2,3,4,5]
r.shuffle(list1) #randomly shuffle the list
print("Shuffled list:", list1)
print("Random odd number:", r.randrange(1,10,2)) #random odd number between 1 and 10

import calendar
  
y = 2026
m = 2
print(calendar.month(y, m))
print ("The calendar of year 2026 is : ") 
print (calendar.calendar(y)) 

import time as t

print("Current time:", t.time()) 
print("Current time:", t.ctime()) 
print("Current time:", t.localtime())

start=t.time()
for i in range (10):
    print(i)
    
end=t.time()
print("Execution time:", end-start)


import os 

cwd = os.getcwd() 
print("Current working directory:", cwd)

path = "C:\\Users\\pavit\\Downloads\\Python"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list)