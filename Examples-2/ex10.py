number=int(input("Enter a positive number:"))

if number>0:
    for i in range(number-1):
        number=number*(i+1)
    print(number)
elif number==0:
    print(1)
