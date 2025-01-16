#with open("a.txt") as file:
#   data = file.read()
#    print(data)

try:
    file = open("day30/a.txt")
    a = {"name": "John", "age": 30}
    print(a["name"])
except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("Hello World")
except KeyError as e:
    print(f"{e} Key not found")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")