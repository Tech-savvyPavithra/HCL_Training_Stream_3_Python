try:
    coupon = "SAVE51"
    valid_coupons = ["WELCOME10", "FESTIVE20", "SAVE50"]

    if coupon not in valid_coupons:
        raise ValueError("Invalid coupon code")

except ValueError as e:
    print("Error:", e)

else:
    print("Coupon applied successfully!")

finally:
    print("Thank you for shopping with us!") 