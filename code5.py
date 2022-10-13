def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
count = 0
while True:
    choice = input("enter operator (add, substract, multiply, divide):")

    if choice in ("add", "substract", "multiply", "divide"):
        input1 = float(input("Enter input1:"))
        input2 = float(input("Enter input2:"))

        if choice == "add":
            print(input1,"+",input2,"=",add(input1,input2))
            count = +1
        elif choice == "substract":
            print(input1,"-",input2,"=",substract(input1,input2))
            count = +1
        elif choice == "multiply":
            print(input1,"*",input2,"=",multiply(input1,input2))
            count = +1
        elif choice == "divide":
            print(input1,"/",input2,"=",divide(input1,input2))
            count = +1

        next_calculation = input("Let's do next calculation? (continue/exit): ")
        if next_calculation == "exit":
            print(count)
            break

""""
        output:
        enter
        operator(add, substract, multiply, divide): add
        Enter
        input1: 4
        Enter
        input2: 5
        4.0 + 5.0 = 9.0
        Let
        's do next calculation? (continue/exit): exit
        1

        Process
        finished
        with exit code 0
"""
