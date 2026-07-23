class people:
    def __init__(self,name,cid,age):
        self.name = name 
        self.cid = cid
        self.age = age
       

class licence:    
    def __init__(self,catagory,phone,dateofbirth,gender):
        self.catagory = catagory
        self.phone = phone
        self.dateofbirth = dateofbirth
        self.gender = gender
       

class LMS:
    def __init__(self):
        self.management={}

    def add_data(self):

        #input people
        name= input("Enter name: ")
        cid = input("Enter Citizenship ID: ")
        age = int(input("Enter age"))

        #input licence
        catagory = input("Enter licence category: ")
        phone = input("Enter phone number: ")
        dateofbirth = input("Enter date of birth:")
        gender = input("Enter gender: ")

        #create object
        p1 = people(name, cid, age)
        l1 = licence(catagory, phone, dateofbirth, gender)

        new_management = {
            "p": p1,
            "l": l1
        }
        
        self.management[len(self.management)+1]=new_management



lms_obj = LMS()
lms_obj.add_data()

for key, each_data in lms_obj.management.items():
    print(each_data["p"].name)
    print(each_data["l"].catagory)