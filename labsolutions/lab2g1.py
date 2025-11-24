sayi=input("Enter the number:")
list1=[]
for i in sayi:
    list1.append(int(i))

if int(sayi)%sum(list1)==0:
    print(f"The number {sayi} is an harshad")
else:
    print(f"The number {sayi} is not an harshad")

