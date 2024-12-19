class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print("Name of the person is " ,self.fname  ,self.lname)

class student(Person):
    def __init__(self, fname, lname ,graduationyear):
        super().__init__(fname, lname)
        self.graduationyear=graduationyear

stud1=student("Raza","Iqbal",2002)
stud1.printname()
print("{} was graduated in the yer {}".format(stud1.fname,stud1.graduationyear))