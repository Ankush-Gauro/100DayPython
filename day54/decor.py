def hello_double_decor(function):
    def wrapper_func():
        #do smth before func
        function()
        function()
        #do smth after func

    return wrapper_func

@hello_double_decor
def say_hello():
    print("Hello")

say_hello()