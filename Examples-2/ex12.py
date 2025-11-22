vowels=["a","e","i","o","u"]

def main():
    word=input("Enter a word:")
    word2=word.lower()
    number_of_vowels(word2)    

def number_of_vowels(x):
    num_of_vowels=0
    a=0
    e=0
    i=0
    o=0
    u=0
    for ch in x:
        if ch in vowels:
            num_of_vowels+=1
            if ch=="a":
                a+=1
            elif ch=="e":
                e+=1
            elif ch=="i":
                i+=1
            elif ch=="o":
                o+=1
            elif ch=="u":
                u+=1
    print("Number of vowels=",num_of_vowels)
    print("a:",a)
    print("e:",e)
    print("i:",i)
    print("o:",o)
    print("u:",u)
        
main()
        
