# Nathan Chatham
#
# P3HW2 - Salary Calculator
# Calculates pay for all employees

# Create variables for total values
total_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0

# Enter employee information here
employees = [
    {
        "name": "Nathan",
        "department": "IT",
        "employeeType": "Full-Time",
        "hoursWorked": 45,
        "payRate": 20
    },
    {
        "name": "Jordan",
        "department": "Sales",
        "employeeType": "Part-Time",
        "hoursWorked": 30,
        "payRate": 15
    },
    {
        "name": "Alex",
        "department": "Customer Service",
        "employeeType": "Full-Time",
        "hoursWorked": 42,
        "payRate": 18
    }
]

# Calculate pay for all employees
for employee in employees:

    name = employee["name"]
    department = employee["department"]
    employeeType = employee["employeeType"]
    hoursWorked = employee["hoursWorked"]
    payRate = employee["payRate"]

    # Count each employee
    total_employees += 1

    # Evaluate overtime
    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        overPay = overtimeHours * (payRate * 1.5)
        regPay = 40 * payRate
    else:
        overtimeHours = 0
        overPay = 0
        regPay = hoursWorked * payRate

    # Calculate gross pay
    grossPay = regPay + overPay

    # Add to the totals
    total_overtime += overtimeHours
    total_regular += regPay
    total_gross += grossPay

    # Display employee information
    print("-------------------------------------")
    print("Employee name:", name)
    print("Department:", department)
    print("Employee type:", employeeType)
    print()

    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<16}{"RegHour Pay":<15}{"Gross Pay"}')
    print("-" * 85)
    print(f'{hoursWorked:<15}{payRate:<12.2f}{overtimeHours:<12}{overPay:<16.2f}{regPay:<15.2f}{grossPay:.2f}')

# Display totals after all employees
print()
print("========== FINAL PAYROLL TOTALS ==========")
print("Total number of employees:", total_employees)
print("Total overtime hours:", total_overtime)
print(f"Total regular pay: ${total_regular:.2f}")
print(f"Total gross pay: ${total_gross:.2f}")
