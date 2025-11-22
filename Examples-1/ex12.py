sayı1=input("Enter a positive number:")
toplam=0
for digit in sayı1:
    toplam +=int(digit)
if int(sayı1)%toplam==0:
    print("harshad")
else:
    print("notharshad")
    

