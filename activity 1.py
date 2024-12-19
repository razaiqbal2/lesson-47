class Person:
    def __init__(self,name,idnum):
        self.name=name
        self.idnum=idnum

    def display(self):
        print("The name of person {} and its id is {}".format(self.name,self.idnum))

class empolyeee(Person):
    def __init__(self, name, idnum , salary , post):
        Person.__init__(self,name,idnum)
        self.salary=salary
        self.post=post
        
emp1=empolyeee("Ali" , 124 ,1700,"Manger")
emp1.display()
print("{} has salary {} and its post is a {}".format(emp1.name,emp1.salary,emp1.post))