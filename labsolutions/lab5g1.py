list1=[1,3,5,4,2,4,2,6]

def increasing_subseq(list1):
    sublists=[]
    temp=[list1[0]]
    for i in range(1,len(list1)):
        if list1[i]>list1[i-1]:
            temp.append(list1[i])
        else:
            if len(temp)>1:
                sublists.append(temp)
            temp=[list1[i]]
    if len(temp)>1:
        sublists.append(temp)
    return sublists

print(increasing_subseq(list1))