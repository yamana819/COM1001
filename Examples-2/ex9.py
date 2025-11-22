number=int(input("Enter a number:"))

def faktoryel(a):
    result=1
    for i in range(1,a+1):
        result *=i
    return result
if number>0:
    print(faktoryel(number))
elif number==0:
    print(1)

        

