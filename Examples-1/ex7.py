a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
	print("{} is the greatest number".format(a))
elif b>a and b>c:
	print("{} is the greatest number".format(b))
else:
	print("{} is the greatest number".format(c))
