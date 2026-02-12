def dis(amt):
    if amt<1000:
        return amt
    elif amt>=1000 and amt<5000:
        return amt-amt*0.05
    elif amt>=5000:
        return amt-amt*0.1
    
amount=int(input("Enter the amount: "))
print("Final payable amount: ",dis(amount))