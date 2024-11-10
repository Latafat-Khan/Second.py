#welcome to tip calculator
#what was the total bill?
#what percentage tip would you like to give?10,12,15?  
#how many people to split the bill?
#each person should pay:

print("welcome to tip calculator")
bill=float(input("what was the total bill?"))
tip=int(input("what percentange tip would you like to give?10,12 or 15?"))
people=int(input("how many people to split the bill?"))

tip_as_percentage=tip/100
total_tip_amount=bill * tip_as_percentage
total_bill=bill + total_tip_amount
bill_per_person=total_bill/people
final_amount=bill_per_person
print(f"each person should pay:{final_amount}")