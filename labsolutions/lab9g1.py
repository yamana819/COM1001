target_words=input("Enter the words to search for:")
name_file=input("Enter the name of file:")
def readInput(fileName):
    infile=open(fileName,'r')
    list1=infile.readlines()
    infile.close()
    for i in range(len(list1)):
        list1[i]=list1[i].rstrip("\n")
        list1[i]=list1[i].rstrip(".")
        list1[i]=list1[i].split(' ')
    for item in list1:
        for j in range(len(item)):
            item[j]=item[j].rstrip(",").lower()
    return list1
liste=readInput(name_file)
liste2=target_words.split(",")
def find_word(liste,liste2):
    for word in liste2:
        flag=True
        for sublist in liste:
            if word.lower() in sublist:
                a=liste.index(sublist)+1
                flag=False
                break
        if flag:
            print("The word",word,"does not exist in file")
        else:
            print("The word",word,"exists in line:",a)
find_word(liste,liste2)