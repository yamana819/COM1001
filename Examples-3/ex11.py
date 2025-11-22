def is_palindrome(word):
    word=word.lower()
    if len(word)<=1:
        return True
    elif word[0]==word[-1]:
        word=word[1:-1]
        return is_palindrome(word)
    else:
        return False
word1=input("enter a word:")
if is_palindrome(word1):
    print("this word is palindrome")
else:
    print("not a palindrome")
