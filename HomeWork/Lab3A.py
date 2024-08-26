current_b = float(input("What's your current credit card balance: "))
APR = float(input("Enter the current APR of your credit card: "))
monthly_per_rate = round(float(APR/12), 3)
min_payment =  round(float(current_b * APR / 12) , 2)

print("\nAmount owned: ", '$', current_b)
print("APR: ", APR)
print("Monthly percentage per month: ", monthly_per_rate)
print("Minimum payment: ", '$', min_payment)