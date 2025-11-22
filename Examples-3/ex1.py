d={}
d["spam"]=3
d.update({"spam":1,"eggs":4})
print(len(d))
print("eggs" in d)
print(list(d.keys()))
print(list(d.values()))
for key in d:
    print(key)
    print(d[key])
print(d.get("toast","not in dictionary"))
print(d.get("eggs","not in dictionary"))
del (d["eggs"])
print(d)
