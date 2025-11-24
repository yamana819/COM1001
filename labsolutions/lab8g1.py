
def permutation(list1):
    if len(list1)==1:
        return [list1]
    else:
        list1.sort()
        permutations=[]
        for i in range(len(list1)):
            if i>0 and list1[i]==list1[i-1]:
                continue
            remaining=list1[:i]+list1[i+1:]
            for perm in permutation(remaining):
                permutations.append([list1[i]]+perm)
        return permutations
liste=[1,2,2,3]
print(permutation(liste))

