def main():
    list1=[1,3,2,4,5,2,1,6]
    buble_sort(list1)
    print(list1)

def buble_sort(lst):
    k=1
    needNext=True
    while k<len(lst) and needNext:
        needNext=False
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                temp=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=temp
                needNext=True
main()    