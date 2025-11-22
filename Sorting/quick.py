def main():
    list1=[1,2,3,2,1,4,5,7,6,8,9]
    quickSort(list1)
    print(list1)

def quickSort(lst):
    quickSortHelper(lst,0,len(lst)-1)

def quickSortHelper(lst,first,last):
    if last>first:
        pivotIndex=partition(lst,first,last)
        quickSortHelper(lst,first,pivotIndex-1)
        quickSortHelper(lst,pivotIndex+1,last)

def partition(lst,first,last):
    pivot=lst[first]
    low=first+1
    high=last
    while high>low:
        while low<=high and lst[low]<=pivot:
            low+=1
        while low<=high and lst[high]>pivot:
            high-=1
        if high>low:
            lst[high],lst[low]=lst[low],lst[low]
    while high>first and lst[high]>=pivot:
        high-=1
    if pivot>lst[high]:
        lst[first]=lst[high]
        lst[high]=pivot
        return high
    else:
        return first
main()