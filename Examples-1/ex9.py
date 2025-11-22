a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
d=int(input("Enter the fourth number:"))
list1=[a,b,c,d]
list2=[13,24,55,68,84]
maxnum=max(list1)
if maxnum in list2:
    print("it exists in second list.")
else:
    print("it does not exist.")

