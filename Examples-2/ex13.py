cost=int(input("Enter the total cost:"))
revenue=int(input("Enter the total revenue:"))
def profit_calculator(num1,num2):
    if num1==revenue:
        print("Break Even")
    elif num1>num2:
        result=cost-revenue
        print("loss is {}".format(result))
    elif num2>num1:
        result=revenue-cost
        print("profit is {}".format(result))

profit_calculator(cost,revenue)
    
