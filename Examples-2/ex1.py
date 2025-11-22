length=int(input("Enter the length of the list:"))
list1=list()
for i in range(length):
    number=int(input("Enter a number:"))
    list1.append(number)

print(round(sum(list1)/len(list1),2))
print("The largest number is", max(list1))
print("The minimum number is",min(list1))

