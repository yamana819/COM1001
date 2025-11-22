class Heap:
    def __init__(self):
        self.lst=[]
    def add(self,e):
        self.lst.append(e)
        currentIndex=len(self.lst)-1

        while currentIndex>0:
            parentIndex=(currentIndex-1)//2
            if self.lst[currentIndex]>self.lst[parentIndex]:
                self.lst[currentIndex],self.lst[parentIndex]=self.lst[parentIndex],self.lst[currentIndex]
            else:
                break
            currentIndex=parentIndex
    def remove(self):
        if len(self.lst)==0:
            return None
        removedItem=self.lst[0]
        self.lst[0]=self.lst[len(self.lst)-1]
        self.lst.pop(len(self.lst)-1)
        currentIndex=0
        while currentIndex<len(self.lst):
            leftChildIndex=2*currentIndex+1
            rightChildIndex=2*currentIndex+2
            if leftChildIndex>=len(self.lst):
                break
            maxIndex=leftChildIndex
            if rightChildIndex<len(self.lst):
                if self.lst[maxIndex]<self.lst[rightChildIndex]:
                    maxIndex=rightChildIndex
            if self.lst[currentIndex]<self.lst[maxIndex]:
                self.lst[maxIndex],self.lst[currentIndex]=self.lst[currentIndex],self.lst[maxIndex]
                currentIndex=maxIndex
            else:
                break
        return removedItem
    def getSize(self):
        return len(self.lst)
    def isEmpty(self):
        return self.getSize==0
    def peek(self):
        return self.lst[0]
    def getList(self):
        return self.lst
def main():
    list1=[-44,-5,-3,3,3,1,-4,0,1,2,4,5,53]
    heapSort(list1)
    print(list1)

def heapSort(lst):
    heap=Heap()
    for v in lst:
        heap.add(v)
    for i in range(len(lst)):
        lst[len(lst)-1-i]=heap.remove()
main()