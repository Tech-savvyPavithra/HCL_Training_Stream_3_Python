def infinite_even():
    num = 0
    while True:
        yield num
        num += 2
        
evens = infinite_even()

n=int(input("Enter the number of even numbers to generate: "))
for _ in range(n):
    print(next(evens))