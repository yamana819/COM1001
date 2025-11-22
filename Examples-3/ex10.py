def power(r,n):
    if n==1:
        return r
    else:
        return r*power(r,n-1)
print(power(2,2))
