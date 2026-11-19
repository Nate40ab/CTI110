
# Nathan Chatham
# 11/19/2026
# P5LAB
# This program simulates a customer using a self-checkout machine.

import random

def disperse_change(change):
    dollars = int(change)
    change = round(change - dollars, 2)

    quarters = int(change / 0.25)
    change = round(change - quarters * 0.25, 2)

    dimes = int(change / 0.10)
    change = round(change - dimes * 0.10, 2)

    nickels = int(change / 0.05)
    change = round(change - nickels * 0.05, 2)

    pennies = int(change / 0.01)

    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)


def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)

    print("You owe $", format(total_owed, ".2f"))

    cash = float(input("How much cash will you put into the self-checkout? "))

    change = round(cash - total_owed, 2)

    disperse_change(change)


main()
