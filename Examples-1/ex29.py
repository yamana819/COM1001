infile=open("inputq3.txt",'r')
list1=infile.readlines()

for i in range(len(list1)):
    list1[i]=list1[i].rstrip("\n")
    list1[i]=list1[i].split(',')

mydict={}
for sublist in list1:
    mydict[sublist[0]]={"city":sublist[1],"championships":int(sublist[2]),"Date of establishment":int(sublist[3])}

print(mydict)
