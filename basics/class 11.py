class student:
    def __init__(self,name,rollno,section,rank):
        self.name = name
        self.rollno = rollno
        self.section = section
        self.rank = rank

    def display(self):
        print("Name:" , self.name)
        print("rollno:", self.rollno)
        print("section:", self.section)
        print("rank:", self.rank)

student1 = student("krimon",10,"abc",20)

student1.display()

