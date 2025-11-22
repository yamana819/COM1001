from tkinter import *
class TurkiyeTeams():
    def __init__(self):
        window=Tk()
        window.title("Teams")
        txtbtn="Display the teams"
        btnDisplay=Button(window,text=txtbtn,command=self.displayTeams)
        btnDisplay.grid(row=0,column=0,columnspan=3,pady=5)
        yscroll=Scrollbar(window,orient=VERTICAL)
        yscroll.grid(row=1,column=1,rowspan=10,pady=5,sticky=NS)
        self.contentteams=StringVar()
        self.listTeams=Listbox(window,width=20,height=8,listvariable=self.contentteams,yscrollcommand=yscroll.set)
        self.listTeams.grid(row=1,column=0,padx=(5,0),pady=(0,5),rowspan=10)
        yscroll["command"]=self.listTeams.yview
        txtlbl="Number of\nteams:"
        Label(window,text=txtlbl).grid(row=1,column=2,padx=10,pady=5)
        self.contentnumteams=StringVar()
        entNumTeams=Entry(window,width=2,state="readonly",textvariable=self.contentnumteams)
        entNumTeams.grid(row=2,column=2)
        window.mainloop()
    def displayTeams(self):
        infile=open("input15.txt",'r')
        teamset={line.split(',')[1].rstrip() for line in infile}
        self.contentteams.set(tuple(sorted(teamset)))
        numteams=len(teamset)
        self.contentnumteams.set(numteams)


TurkiyeTeams()
