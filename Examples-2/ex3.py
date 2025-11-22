def main():
    file="superlig.txt"
    displaywithforloop(file)
    print()
    displaywithlistcomprehension(file)
    print()
    displaywithreadline(file)
    
def displaywithforloop(a):
    infile=open(a,'r')
    for line in infile:
        print(line, end='')
    infile.close()
    
def displaywithlistcomprehension(a):
    infile=open(a,'r')
    listclups=[line.rstrip() for line in infile]
    infile.close()
    print(listclups)

def displaywithreadline(a):
    infile=open(a,'r')
    line=infile.readline()
    while line!='':
        print(line,end='')
        line=infile.readline()
    infile.close()

main()
