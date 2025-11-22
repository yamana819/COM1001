def main():
    phonetic_alphabet={'a':"alpha",'b':"bravo",'c':"charlie"}
    
    while True:
        try:
            letter=input("Enter a,b or c:")
            print(phonetic_alphabet[letter])
            break
        except KeyError:
            print("please enter a,b or c")

main()
