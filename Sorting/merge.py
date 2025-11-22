def main():
    list1=[1,3,2,3,2,4,7,6,9,8]
    mergeSort(list1)
    print(list1)


def mergeSort(lst):
    if len(lst)>1:
        firstHalf=lst[:len(lst)//2]
        mergeSort(firstHalf)
        secondHalf=lst[len(lst)//2:]
        mergeSort(secondHalf)
        merge(firstHalf,secondHalf,lst)

def merge(list1,list2,temp):
    current1=0
    current2=0
    current3=0
    while current1<len(list1) and current2<len(list2):
        if list1[current1]<list2[current2]:
            temp[current3]=list1[current1]
            current1+=1
            current3+=1
        else:
            temp[current3]=list2[current2]
            current2+=1
            current3+=1
    while current1<len(list1):
        temp[current3]=list1[current1]
        current1+=1
        current3+=1
    while current2<len(list2):
        temp[current3]=list2[current2]
        current2+=1
        current3+=1

main()