def main():
    list1=[1,4,3,7,2,5]
    insertion_sort(list1)
    print(list1)

def insertion_sort(lst):
    for i in range(1,len(lst)):
        k=i-1
        current_element=lst[i]
        while k>=0 and lst[k]>current_element:
            lst[k+1]=lst[k]
            k-=1
        lst[k+1]=current_element

main()
