# Nathan Chatham
# 9.17.26
# P1HW1
# preforme mathematical equations 

print("-----Calculating Exponenets-----")

base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

#calculate

true_value = base_value ** exponent

print(base_value, "raised to the power of", exponent, "is", true_value )


print("-----Addition and Subtraction-----") 

Starting_integer = int(input("Enter a starting integer: "))
Addition_integer = int(input("Enter a integer to add: "))
Subtraction_integer = int(input("Enter an integer to subtract: "))

Correct_answer = Starting_integer + Addition_integer - Subtraction_integer

print(Starting_integer, "+", Addition_integer, "-", Subtraction_integer, "is equal to:", Correct_answer )
