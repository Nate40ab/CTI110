# Nathan Chatham
#
# Use a loop to calculate pay for ALL employees
# P3HW2- Salary Calculator

# Create variables for the total values that display upon done
total_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0

# request employee information
name = input("Enter employee's name: ")

while name != "Done":

    # Count each employee
    total_employees += 1

    hoursWorked = float(input("Enter number of hours worked: "))

    payRate = float(input("Enter employee's pay rate: "))

    # evaluate overtime
    if hoursWorked > 40:

        # calculate overtime
        overtimeHours = hoursWorked - 40

        # Calculate overPay
        overPay = overtimeHours * (payRate * 1.5)

        # calculate salary for reg hours
        regPay = 40 * payRate

        # calculate gross pay
        grossPay = regPay + overPay

    else:
        overPay = 0
        overtimeHours = 0

        regPay = hoursWorked * payRate
        grossPay = regPay

    # Add to the totals
    total_overtime += overtimeHours
    total_regular += regPay
    total_gross += grossPay

    # Display output
    print("-------------------------------------")
    print("Employee name:  ", name, "\n")

    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12}{overPay:<20}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')

    name = input("Enter another employee or Done to quit: ")

# Display totals after the loop ends
print()
print("Total number of employees:", total_employees)
print("Total overtime hours:", total_overtime)
print(f"Total regular pay: ${total_regular:.2f}")
print(f"Total gross pay: ${total_gross:.2f}")