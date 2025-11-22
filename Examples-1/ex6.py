niceletters=['A','F','Y']
input1=input("Enter a word:")
c=0
for a in niceletters:
    input1.upper()
    if a in input1:
        c+=1 
if c!=0:
    print("This word includes {} of niceletters.".format(c))
else:
    print("This word includes no niceletters.")


        
