pop=310000
print("{0:10} {1}".format("Year","Population"))
for year in range(2014,2020):
    print("{0:10d} {1: ,d}".format(year,round(pop)))
    pop +=0.03 * pop
    
