import pickle
infile=open("q4t.dat",'rb')
d1=pickle.load(infile)
infile.close()
print(d1)
