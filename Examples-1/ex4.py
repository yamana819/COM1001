gpa=eval(input("Enter your gpa:"))
if gpa >=3.9:
    honors="takdirname"
elif gpa >=3.6:
    honors="tesekkurname"
elif gpa >=3.3:
    honors="nothing"
else: 
    honors="siktirname"
print("You graduated with" +"",honors)

