def recursiveFactorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*recursiveFactorial(num-1)
    
print(recursiveFactorial(6))

