num1=input("enter first number:")
num2=input("enter second number:")


if num1.isdigit() and num2.isdigit():
    print("the sum is", str(eval(num1)+eval(num2))+ ".")
elif not num1.isdigit():
    if not num2.isdigit():
        print("Neither entry was a proper number.")
    else:
        print("the first entry was not a proper number.")
else:
    print("the second entry was not a proper number")
    
