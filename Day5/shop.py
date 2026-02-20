from functools import reduce
def final_bill(prices):
     dis = map(lambda x: x*0.9, prices)
     fil = filter(lambda x: x>=200, dis)
     red = reduce(lambda x,y: x+y, fil)
     return red

n = int(input("Enter number of products: "))
prices = []
for _ in range(n):
    prices.append(float(input("Enter price: ")))

print("Final bill:", final_bill(prices))
