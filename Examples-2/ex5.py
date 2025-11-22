def main():
    kume=createlist('superlig.txt')
    sortlistalpha(kume)

def createlist(filename):
    infile=open(filename,'r')
    desiredlist=[line.rstrip() for line in infile]
    infile.close()
    return desiredlist

def sortlistalpha(a):
    a.sort()
    for i in range(len(a)):
        a[i]=a[i]+'\n'
    outfile=open('takimlar.txt','w')
    outfile.writelines(a)
    outfile.close()

main()
    
