def main():
    game_name=input("Enter the name of game:")
    d1=create_dict("q3t.txt")
    print(find_character(d1,game_name))


def create_dict(fileName):
    infile=open(fileName,'r')
    list1=infile.readlines()
    infile.close()
    for i in range(len(list1)):
        if '\n' in list1[i]:
            list1[i]=list1[i].rstrip('\n')
        list1[i]=list1[i].split(',')
    return dict(list1)

def find_character(d1,name):
    if name in list(d1.keys()):
        return d1[name]
    else:
        game_name=input("please enter another name of game:")
        return find_character(d1,game_name)

main()
