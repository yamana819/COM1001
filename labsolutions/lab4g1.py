word1=input("Enter a word:")
word2=input("Enter the second word:")

def common_letter(w1,w2):
    list1=[]
    for i in w1:
        if i in w2:
            if i not in list1:
                list1.append(i)
    return tuple(list1)

def seperate_letter(w1,w2):
    list2=[]
    for i in w1:
        if i not in w2:
            if i not in list2:
                list2.append(i)
    return tuple(list2)

commons=common_letter(word1,word2)
letters1= seperate_letter(word1,word2)
letters2=seperate_letter(word2,word1)
print(commons)
print(letters1)
print(letters2)