liste=["afy","monur","aamet","kayabasi","onr"]

def create_dict(list1):
    dict_required={}
    for word in list1:
        if len(word) not in dict_required:
            dict_required[len(word)]=[word]
        else:
            dict_required[len(word)].append(word)
    return dict(sorted(dict_required.items()))


print(create_dict(liste))