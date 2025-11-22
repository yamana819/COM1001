def main():
    first_word=input("Enter the first word:")
    second_word=input("Enter the second word:")
    print(tuple(common_character(first_word,second_word)))
    print(tuple(characters_first(first_word,second_word)))
    print(tuple(characters_second(first_word,second_word)))

def common_character(a,b):
    a.strip()
    b.strip()
    list1=[]
    for ch in a:
        if ch not in list1:
            if ch in b:
                if ch==' ':
                    continue
                else:
                    list1.append(ch)
    return list1

def characters_first(a,b):
    list2=[]
    a.strip()
    b.strip()
    for ch in a:
        if ch not in b:
            list2.append(ch)
    return list2

def characters_second(a,b):
    a.strip()
    b.strip()
    list3=[] 
    for ch in b:
        if ch not in a:
            list3.append(ch)
    return list3
    
main()
            
            







