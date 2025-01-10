print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 15 18 20 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
percent_total = bill * tip_percent
final_bill = bill + percent_total
person_amount = final_bill / people
final_amount = round(person_amount, 2)
print(f'Each person pays {final_amount} dollars')
