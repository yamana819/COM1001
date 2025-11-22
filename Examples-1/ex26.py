firstNumber=eval(input("Enter the first number:"))
secondNumber=eval(input("Enter the second number:"))
thirdNumber=eval(input("Enter the third number:"))
max=firstNumber
if secondNumber>max:
    max=secondNumber
if thirdNumber>max:
    max=thirdNumber
print("The largest number is", str(max) + ".")

