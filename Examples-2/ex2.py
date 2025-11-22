cafein=int(input("Enter the amount of cafein:"))
a=0
while True:
    a+=1
    cafein=cafein - ((cafein*13)/100)
    if cafein<= 65:
        break
print(a)
print(round(cafein*((87/100)**24),2))
       
    
    
    
    

