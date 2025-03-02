from bs4 import BeautifulSoup

with open('day45/bs4-start/web.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())
print(soup.a)