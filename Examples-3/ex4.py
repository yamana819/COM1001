import pickle
dct1={1:"Afy",2:"Kaan",3:"Zekeriya",4:"Ahmet Mete"}
outfile=open("q4t.dat",'wb')
pickle.dump(dct1,outfile)
outfile.close
