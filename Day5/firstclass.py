def multiplier(k):
    def multiply(x):
        return x * k   
    return multiply

d = multiplier(2)
t = multiplier(3)

print(d(10))
print(t(10))