from tkinter import *
def displayResult():
    global result
    if not entQuestion.get().rstrip():
        result="Please enter a question"
    elif lstCategories.get(lstCategories.curselection())=="History":
        result="History takes us deep into the past!"
    elif lstCategories.get(lstCategories.curselection())=="General":
        result="That is a great general question!"
    elif lstCategories.get(lstCategories.curselection())=="Science":
        result="A scientific question, it could lead to discoveries."
    elif lstCategories.get(lstCategories.curselection())=="Games":
        result="You can learn a lot about this game!"
    content2.set(result)
window=Tk()
content2=StringVar()
categories=["History","General","Science","Games"]
content1=StringVar()
content1.set(tuple(categories))
window.title("Ask Question")
lstCategories=Listbox(window,width=10,height=5,listvariable=content1)
lstCategories.grid(row=0,column=0,padx=5,pady=4)
entQuestion=Entry(window,width=40)
entQuestion.grid(row=0,column=1)
btnQuestion=Button(window,text="Ask",command=displayResult)
btnQuestion.grid(row=0,column=2,padx=5,pady=5)
entResult=Entry(window,width=50,state="readonly",textvariable=content2)
entResult.grid(row=1,column=0,columnspan=3,padx=25,pady=30)
window.mainloop()