def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Denominator cannot be zero"

cont = 1
while(cont!=0):
    print("\n")
    print("----------Calculator------------\n")
    print("1. Press 1 for Addition")
    print("2. Press 2 for Subtraction")
    print("3. Press 3 for Multiplication")
    print("4. Press 4 for Division")
    print("5. Press 5 to Exit")
    print("\n")

    choice = int(input("Enter your choice from the above options : "))

    if choice==1:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(add(a,b))
        cont = int(input("Do you want to continue ? Press 1 for yes and 0 for no: "))

    elif choice==2:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(subtract(a,b))
        cont = int(input("Do you want to continue ? Press 1 for yes and 0 for no: "))

    elif choice==3:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(multiply(a,b))
        cont = int(input("Do you want to continue ? Press 1 for yes and 0 for no: "))

    elif choice==4:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(divide(a,b))
        cont = int(input("Do you want to continue ? Press 1 for yes and 0 for no: "))

    elif choice==5:
        print("Thank You!!")
        exit(1)

    else:
        print("Enter a valid choice")
        cont = 1