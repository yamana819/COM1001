def main():    
    both=appendlist('champs.txt')
    printoutfile(both,'superlig.txt','sampiyonlar.txt')
    
def appendlist(filename):
    infile=open(filename,'r')
    desiredlist=[line.rstrip() for line in infile]
    infile.close()
    return desiredlist

def printoutfile(listname,oldfile,newfile):
    infile=open(oldfile,'r')
    outfile=open(newfile,'w')
    for team in infile:
        if team.rstrip() in listname:
            outfile.write(team)
    infile.close()
    outfile.close()

main()
