cost=eval(input("Enter the total counts:"))
revenue=eval(input("Enter the total revenue:"))
if cost==revenue:
    resul="Break even"
else:
    if cost<revenue:
        profit=revenue-cost
        result="profit is {0:,.2f}. $".format(profit) 
    else:
        loss=count-revenue
        result="loss is {0:,.2f}.".format(loss)    
print(result)

