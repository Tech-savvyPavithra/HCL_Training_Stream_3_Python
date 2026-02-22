def accumulator(start=0):
    total = start          

    def add(value):
        nonlocal total     
        total += value
        return total

    return add

acc1 = accumulator(10)
acc2 = accumulator(100)

print(acc1(5))    # 10 + 5
print(acc1(20))   # 15 + 20
print(acc1(-3))   # 35 - 3

print(acc2(50))   # 100 + 50
print(acc2(25))   # 150 + 25