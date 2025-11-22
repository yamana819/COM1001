def pay(wage,hours):
    if hours<=40:
        amount=hours*wage
    else:
        amount=(wage*40) + ((1.5)*wage*(hours-40))
    return amount
hourlyWage=eval(input("Enter the hourly wage:"))
hoursWorked=eval(input("Enter the number of hours worked:"))
print("Earnings: ${0:,.2f}".format(pay(hourlyWage,hoursWorked)))

    

