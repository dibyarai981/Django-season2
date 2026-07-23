#n=10
#for i in range(n):
 # print(i)

#name = ["ruzal","dibya","krimin"]

#for i,val in enumerate(name):
#print(i,"*",val)

people={
    "name":"krimon",
    "age":"20",
    "collage":"IIC",
    "Course":"BIT",
    "Work":"Intern",
    "email": "krimongurung19@gmail.com"
}

for key,val in people.items():
    print(key,val)

    print(people.get(key,"Email not found"))

