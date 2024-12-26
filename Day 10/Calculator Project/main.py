import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calculation = {'+': add, '_':subtract, '*':multiply,'/':divide}

calculate = True
num1 = int(input("What is the first number: "))
while calculate:
    operation = input("What operation you wanna perform [\'+\',\'-\',\'*\',\'/\']:")
    num2 = int(input("Pick you second number: "))
    result = calculation[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {result}")
    choice = input(f"Type \'y\' to continue operation with {result} or type \'n\': ")
    if choice == 'y':
        num1 = result
    if choice == 'n':
        calculate = False

