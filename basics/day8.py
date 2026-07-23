#import function
from basics.function import add ,subtraction,multiply,divide

    
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")

    choice = int(input("Enter 1 to 4:    "))

    if choice in [1, 2, 3, 4]:
        num1= float(input("Enter first number:"))
        num2= float(input("Enter second number: "))
        break



if choice == 1:
    print("Result =", add(num1 , num2))
    

elif choice ==2:
    print("Result =", subtraction(num1 , num2))

elif choice ==3:
    print("Result =", multiply(num1 , num2 ))

elif choice ==4:
    print("Result =", divide(num1 ,num2))

else: 
    print("Noting found ")
            

