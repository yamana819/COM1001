count=0
total=0
print("Enter -1 to terminate entering numbers.")
num=eval(input("Enter a nonnegative number:"))
min=num
max=num
while num !=-1:
    count +=1
    total +=num
    if num<min:
        min=num
    if num>max:
        max=num
    num=eval(input("Enter a nonnegative number"))
if count>0:
    print("Minimum:", min)
    print("Maximum:", max)
    print("Average:", total/count)
else:
    print("No nonnegative number were entered.")

        
    

