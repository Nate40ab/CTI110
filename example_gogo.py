#create some float variables for the adoption cost
dog_fee = 80.99
penguin_fee = 8000.00
parrot_fee = 2000.99
lizard_fee = 20.99


#create some interger variables

dog_quantity = 8
penguin_quantity = 4
parrot_quantity = 10
lizard_quantity = 25

#display usuing string format

print(f"{'ANIMAL TYPE':<16}{'ADOPTION FEE':<17}{'QUANTITY':<16}")
print("-"*80)
print(f"{'Dog':<16}${dog_fee:<17,.2f}{dog_quantity:<16}")

print(f"{'penquin':<16}${penguin_fee:<17,.2f}{penguin_quantity:<16}")

print(f"{'parrot':<16}${parrot_fee:<17,.2f}{parrot_quantity:<16}")

print(f"{'lizard':<16}${lizard_fee:<17,.2f}{lizard_quantity:<16}")






