def add(a,b):
    return a+b

def calculate(function, a, b):
    result = add(a,b)
    print(result)

calculate(add,1,2)

def outer():
    print("I am outer")

    def inner():
        print("Scope is only inside outer function")

    return inner

inner = outer()
inner()