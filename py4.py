def add():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Addition is {n1 + n2}")
    
def sub():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Subtraction is {n1 - n2}")

def mul():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"Multiplication is {n1 * n2}")

def div():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"Division is {n1 / n2}")

while True:
    print("\nSelect any option: +  -  /  *")
    print("Type 'exit' to quit")

    op = input("Enter the option to perform: ")

    if op == "exit":
        print("Calculator closed")
        break

    elif op == "+":
        add()

    elif op == "-":
        sub()

    elif op == "*":
        mul()

    elif op == "/":
        div()

    else:
        print("Invalid input")