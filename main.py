# TIP CALCULATOR PROGRAM

total_bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
result_bill = round(total_bill / num_of_people, 2)
total_bill_with_tip = round(result_bill * (percentage / 100 + 1), 2)

print(f"Each person should pay: ${total_bill_with_tip}")