list1=input().split()
list2=[]
list3=[]
for i in range(len(list1)):
    list2.append(int(list1[i]))
average=(sum(list2))/len(list1)
for a in list2:
    if a<average:
        list3.append(str(a))
print(", ".join(list3),"these grades are less than average.")
print(round(len(list3)/len(list1)*100, 2),"is the percentage of the numbers that are less than average.") 

    

