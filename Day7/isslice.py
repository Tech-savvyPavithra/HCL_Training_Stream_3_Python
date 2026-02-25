import itertools

def multiples_of_three():
    num = 0
    while True:
        yield num
        num += 3


first_five = itertools.islice(multiples_of_three(), 5)

for value in first_five:
    print(value)