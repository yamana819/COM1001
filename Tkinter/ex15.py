from tkinter import *

def displayTeams():
    infile=open("input15.txt",'r')
    teamSet={line.split(",")[1].rstrip() for line in infile}
    infile.close()
    contentlst.set(tuple(sorted(teamSet)))
    numTeams=len(teamSet)
    contentnum.set(numTeams)

window=Tk()
window.title("State Teams")
textbtn="Display the teams in Turkiye"
btnDisplay=Button(window,text=textbtn,command=displayTeams)
btnDisplay.grid(row=0,column=0,columnspan=3,pady=5)
yscroll=Scrollbar(window,orient=VERTICAL)
yscroll.grid(row=1,column=1,rowspan=10,pady=(0,5),sticky=NS)
contentlst=StringVar()
lstTeams=Listbox(window,width=20,height=8,listvariable=contentlst,yscrollcommand=yscroll.set)
lstTeams.grid(row=1,column=0,padx=(5,0),pady=(0,5),rowspan=10)
yscroll["command"]=lstTeams.yview
textlbl="Number of\ndifferent\nteams:"
Label(window,text=textlbl,).grid(row=1,column=2,padx=10,pady=5)
contentnum=StringVar()
entNum=Entry(window,width=2,state="readonly",textvariable=contentnum)
entNum.grid(row=2,column=2)
window.mainloop()