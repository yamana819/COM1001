def occuringVowels(word):
    word=word.upper()
    vowels=['A','F','Y']
    includedVowels=[]
    for vowel in vowels:
        if (vowel in word) and (vowel not in includedVowels):
            includedVowels.append(vowel)
    return includedVowels
word=input("Enter a word:")
print("The following vowels occur in the word:"," ".join(occuringVowels(word)))
