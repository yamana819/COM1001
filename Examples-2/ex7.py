def main():
    nums=append_list()
    iseven_odd(nums)

def append_list():
    length=int(input("Enter the length of the list:"))
    numbers=[]
    for i in range(length):
        number=int(input("Enter a number:"))
        numbers.append(number)
    return numbers
def iseven_odd(nums):
    evens=[]
    odds=[]
    for i in nums:
        if i%2==0:
            evens.append(i)
        elif i%2==1:
            odds.append(i)
    print("These are the even numbers in the list:", evens)
    print("These are the odd numbers in the list:", odds)

main()
