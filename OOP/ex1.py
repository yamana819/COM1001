class Student:
    def __init__(self,name="",midterm=0,final=0):
        self.name=name 
        self.midterm=midterm
        self.final=final
    def setName(self,name):
        self.name=name
    def setMidterm(self,midterm):
        self.midterm=midterm
    def setFinal(self,final):
        self.final=final
    def getName(self,name):
        return self.name
    def __str__(self):
        return "name:"+self.name+" midterm:"+str(self.midterm)+" final:"+str(self.final)+" semgrade:"+self.calcSemGrade()
    
class lgStudent(Student):
    def calcSemGrade(self):
        average=round((self.final*6+self.midterm*4)/10)
        if average >= 90:
            return 'A'
        elif average>=80:
            return 'B'
        elif average>=70:
            return 'C'
        elif average>=60:
            return 'D'
        else:
            return 'F'
    
student=lgStudent()
student.setName("Ahmet Furkan Yaman")
student.setMidterm(88)
student.setFinal(82)
print(student)