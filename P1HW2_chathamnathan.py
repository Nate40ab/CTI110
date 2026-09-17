# Nathan Chatham
# 9.17.26
# P1HW2
# calculate travel expenses 
 
print("-----This program calculates and displays travel expenses------")

budget_value = int(input("Enter amount as budget value: "))
travel_loc = input("Enter travel destination: ")
fuel_estimate = int(input("Enter estimated dollar amount for gas usage: "))
hotel_estimate = int(input("Enter estimated amount for acccomodation/resort: "))
food_estimate = int(input("Enter estimated amount for food: "))                         
leftover_funds = budget_value - fuel_estimate - hotel_estimate- food_estimate

print("----Travel Expenses----")
print("location:",travel_loc)
print("Initial Budget:",budget_value)
print("fuel:",fuel_estimate)
print("Accomodation",hotel_estimate)
print("food:", food_estimate)
print()
print()
print("Remaining Balance:",leftover_funds)






                