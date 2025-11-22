def main():
    liste1= add_element()
    element_duplicate(liste1)
    liste2= add_element()
    element_duplicate(liste2)

    print(liste1)
    print(liste2)
    print(is_subset(liste1,liste2))

def add_element():
    list1=input("Enter the numbers:").split()
    return [int(i) for i in list1]

def remove_element(liste,val):
    while val in liste:
        liste.remove(val)

def element_duplicate(liste):
    unique=set(liste)
    for item in liste:
        sayı=liste.count(item)
        if sayı>1:
            remove_element(liste,item)

def is_subset(list1,list2):
    flag= True 
    for i in range(len(list2)):
        if list2[i] in list1:
            continue
        else:
            flag= False 
            break
    return flag
main()
