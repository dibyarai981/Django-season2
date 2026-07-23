dis ={}
name=input("enter your name:")
age=int(input("enter your age:"))
BP=int(input("enter your BP:"))

dis["name"]=name
dis["age"]=age
dis["BP"]=BP

if dis["age"] >= 18:
    print(dis["name"],"👍🏻You are an adult and is Eligible👍🏻")

else:
    print(dis["name"],"Result:""👎🏻You are a minor and not eligible👎🏻")

if dis["BP"] > 120:
    print("Result:""👨🏻‍⚕️ High BP consult to a doctor 👨🏻‍⚕️")

elif dis["BP"] < 90:
    print("Result:""👨🏻‍⚕️ Low BP consult a  doctor 👨🏻‍⚕️ ")

else:
    print("Result:""Noraml Bp")