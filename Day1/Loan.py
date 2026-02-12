def loan_decision(income, credit_score, existing_debt):
    if income >= 50000 and credit_score >= 700 and existing_debt <= 20000:
        return "Eligible"
    elif income >= 30000 and credit_score >= 600 and existing_debt <= 40000:
        return "Review"
    else:
        return "Reject"

income = int(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))
existing_debt = int(input("Enter your existing debt: "))

print(loan_decision(income, credit_score, existing_debt)) 
