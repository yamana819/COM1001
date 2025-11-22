import random
emperors=["Geralt","Aegon","Jinx","Ekko"]
print(random.choice(emperors))
print(random.sample(emperors,3))
a=(random.randint(0,3))
print(emperors[a])
random.shuffle(emperors)
print(emperors[a])
