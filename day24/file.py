file = open("day24/file.txt")

contents = file.read()
print(contents)
file.close()


with open("day24/file.txt", mode="w") as file:
    file.write("New text.")

"""Here all the contents of the file will be replaced with the new text. If you want to add text to the file, you can use mode="a" instead of mode="w".

The with keyword is used to open the file and automatically close it when the block of code is done executing. This is a better practice than manually closing the file using file.close().

If the file does not exist, it will be created. If the file already exists, it will be overwritten."""

with open("day24/file.txt") as file:
    contents = file.read()
    print(contents)