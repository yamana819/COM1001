number=str(input("Enter a number:"))
reversednumber=""
for digit in number:
    reversednumber= digit + reversednumber
if int(reversednumber)*4==int(number):
    print("It is a special number.")
else:
    print("Not a special number.")

    

    
