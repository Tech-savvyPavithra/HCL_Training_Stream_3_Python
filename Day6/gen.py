def count_up_to(n):
    for i in range(1, n + 1):
        yield i
        
n=int(input("Enter a number: "))

for num in count_up_to(n):
    print(num)