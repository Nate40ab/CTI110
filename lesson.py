#define the main function
#the code for the entire program goes in the main

global_variable = "hi"

def get_area_cost(area, cost):
    total_cost=area * cost
    return total_cost


#define a function that calculate area
#it must accept 2 perameters - length & width
def get_area(length, width):
    area= length * width
    return area


def main():
    print("The program is runing:)")
# call the function to get area 
get_area(7,3)
print(f"the area is {area} from inside the main")
cost = float(input("enter cost per unit: "))
total_cost = get_area_cost(area,cost)

print(f"the total cost is ${total_cost:.2f}")

#call the main function
if __name__=="__main__":
    main()