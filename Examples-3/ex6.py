try:
    numDependents=int(input("Enter number of independents"))
except ValueError:
    print("\n you didn't respond with an integer value")
    print("We will assume that your number is 0")
    numDependents=0
taxCredit=1000*numDependents
print(taxCredit)
