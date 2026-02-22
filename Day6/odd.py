def fun(num):
    if num % 2 != 0:        
        print("Odd number")
    else:
        print("Even number")

a = fun
a(80)
a(9)
a(11)


def greet(name1, name2="REC"):
    print(f"Hello {name1} Welcome to {name2}!")
    
dum = greet
    
dum("Pavithra")


def outer():
    x = 10
    
    def inner():
        print(x)  
    
    return inner

f = outer()   
f()  # This will print 10


def outer():
    x = 10
    
    def inner():
        print(x)  
    
    return inner()

f = outer()   
print(f)      # This will print 10 and then None because inner() is called inside outer() and it does not return anything, so f will be assigned the value of None.