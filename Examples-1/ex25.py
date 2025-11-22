list1=["Barcelona","Real Madrid","Manchester City","Bayern Münich"]
list2=['23','27','36','38']
list2.reverse()
en_iyi=[]
en_kotu=[]
for i in range(2):
    en_iyi.append(list1[i])
    en_iyi.append(list2[i])
for i in range(-2,0):
    en_kotu.append(list1[i])
    en_kotu.append(list2[i])

print(tuple(en_iyi))
print(tuple(en_kotu))

