# Nathan Chatham
# 9/21/2026
# Use dictinaries to determine fuel needed

# Create a dictinaries where keys are car names & values are MPG
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Display the dictionary
print(cars.keys())

# Get one of the cars from the user
chosen_vehicle = input("what car would you choose?")

# Pull the mpg associated with chosen_vehicle
mpg_selection = cars[chosen_vehicle]

#Display chosen car and its mpg
print(f"The {chosen_vehicle} gets {mpg_selection} mpg.") 

#Get miles from the user
miles = float(input(f"How many miles will you drive in the {chosen_vehicle}?"))

# calculate gallons of gas needed

fuel_estimate = (miles/mpg_selection)
print(f"to drive the {chosen_vehicle} {miles} miles you will need {fuel_estimate:.2f} gallons of gas")










