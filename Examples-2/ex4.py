def main():
    outfile=open("superlig4.txt",'w')
    createwithwritelines(outfile)
    outfile=open("superlig3",'w')
    createwithwrite(outfile)

def createwithwritelines(a):
    list1=['Galatasaray','Fenerbahce','Besiktas','Alanyaspor','Samsunspor']
    a.writelines(list1)
    a.close()
    
def createwithwrite(a):
    a.write("Galatasaray\n")
    a.write("Besiktas\n")
    a.write("Fenerbahce\n")
    a.close()

main()


        
