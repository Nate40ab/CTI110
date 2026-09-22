# Nathan Chatham
# 9/22/26
#first program usuing lists

# Get three inputs from the user

cost1 = float(input("Enter the price of first item cost: $"))
cost2 = float(input("Enter the price of second item cost: $"))
cost3 = float(input("Enter the price of third item cost: $"))

# create a list holding user inputs

items = [cost1, cost2, cost3]


# print the list
print(items)

# use the sum function to ad all the values in the list

total_price = sum(items)
# display total_price

print(f"Total cost for all items is ${total_price:.2f}")

print(f"the highest value in the list is ${max(items):.2f}")

print(f"the lowest value in the list is ${min(items):.2f}")
 
print()



#Add an item to the pre-existing list
items.append(float(input("enter cost of random item: $")))


print(items)

#display item at index 0
print(f"the price of your first item was: {items[0]}")

#get the number of items in the list 
print(f"total number of items in list: {len(items)}")