class student:
    def __init__(self,name,age,section,school):
        self.name = name
        self.age = age
        self.section = section 
        self.school = school
    
    def __str__(self):
        return f"{self.name,self.age,self.section,self.school}"


class teacher:
    def __init__(self,date,subject,time):
        self.date = date
        self.subject = subject 
        self.time = time
    
    def __str__(self):
        return f"{self.date,self.subject,self.time}"

class SMS:
    def __init__(self):
        self.management={}

    def add_data(self):

        name= input("Enter your name: ")
        age= int(input("Enter your age: "))
        section= input("Enter your section: ")
        school= input("Enter your school: ")

        date= int(input("Enter date: "))
        subject= input("Enter your subject: ")
        time= int(input("Enter time: "))

        s1= student(name,age,section,school)
        t1= teacher(date,subject,time)

        new_management = {
            "s": s1,
            "t": t1
        }

        self.management[len(self.management)+1]=new_management


sms_obj= SMS()
sms_obj.add_data()

for key, each_data in sms_obj.management.items():
    print(each_data["s"])
    print(each_data["t"])