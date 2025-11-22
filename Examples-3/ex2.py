def main():
    print(create_dict("q2t.txt"))
    


def create_dict(textfile):
    infile=open(textfile,'r')
    list1=infile.readlines()
    for j in range(len(list1)):
        if '\n' in list1[j]:
            list1[j]=list1[j].rstrip('\n')
    list2=[item.split(',') for item in list1]
    for i in range(len(list2)):
        list2[i]=tuple(list2[i])
    return dict(list2)
main()
