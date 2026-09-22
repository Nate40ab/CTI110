# Nathan Chatham
#9/22/2026
#P2HW2
#this program will be used to enter and calculate test grades for the following modules

module_1 = float(input("Enter grade for module 1: "))
module_2 = float(input("Enter grade for module 2: "))
module_3 = float(input("Enter grade for module 3: "))
module_4 = float(input("Enter grade for module 4: "))
module_5 = float(input("Enter grade for module 5: "))
module_6 = float(input("Enter grade for module 6: "))



#create a list holding user inputs 
items = [module_1, module_2, module_3, module_4, module_5, module_6]
#print the list out
print(items)


# use the sum function to ad all the values in the list
Overall_grade = sum(items)
#Display Overall_grade


print(f"Total grade for all modules is {Overall_grade:.2f}")
print(f"the highest grade in the list is {max(items):.2f}")
print(f"the lowest grade in the list is {min(items):.2f}")

#Calculate the Average overall grade
average = sum(items)/len(items)

#display item at index 0
print(f"the average of the grades is: {average:.2f}")


#get the number of grades in the list 
print(f"total number of grades in list: {len(items)}")
