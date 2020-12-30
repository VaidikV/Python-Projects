
print("Welcome to the tip calculator!")
bill = float(input("What was the final bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

final_tip = bill * tip / 100
final_bill = (bill + final_tip) / people
final_bill_rounded = round(final_bill, 2)

print(f"Each person should pay: ${final_bill_rounded:.2f}")