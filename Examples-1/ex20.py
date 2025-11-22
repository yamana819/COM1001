years=eval(input("Enter the number of years:"))
cobalt=eval(input("Enter the amount of cobalt:"))
a=0
for a in range(years):
    result=cobalt-((cobalt*12)/100)
    cobalt=round(result)
    a+=1
    print(round(result, 2))

