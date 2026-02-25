def make_counter(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c = make_counter(0)

print(c())  
print(c()) 
print(c())  