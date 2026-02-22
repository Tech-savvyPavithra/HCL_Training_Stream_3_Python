def counter():
    cnt = 0          

    def next():
        nonlocal cnt  
        cnt += 1
        return cnt  

    return next

c = counter()

print(c())
print(c())
print(c())
print(c())
print(c())