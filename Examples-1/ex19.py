a=float(input("Enter a number:"))
x=int(input("Enter the number of repeats:"))
b=0
for b in range(x):
    sonuc=a+((a*5)/100)
    b+=1
    a=sonuc
    print(sonuc)


