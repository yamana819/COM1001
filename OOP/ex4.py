class Student:
    def __init__(self,name,midterm,final):
        self.midterm=midterm
        self.final=final
        self.average=int((self.midterm*4+self.final*6)/10)
        self.name=name
    def average(self):
        return int(self.midterm*4+self.final*6)/10
    def lettergrade(self):
        if self.average>90:
            return "A"
        elif self.average>80:
            return "B"
        elif self.average>70:
            return "C"
        elif self.average>60:
            return "D"
        else:
            return "F"
    
    def __str__(self):
        return self.name+" "+ str(self.average) +" "+self.lettergrade()
carryon="Y"
listofstudents=[]
while carryon=="Y":
    name=input("Enter the name of student: ")        
    midterm=int(input("Enter the midterm grade: "))
    final=int(input("Enter the final grade: "))
    student=Student(name,midterm,final)
    listofstudents.append(student)
    carryon=input("Enter Y/N:")

for st in listofstudents:
    print(st)

