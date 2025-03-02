from bs4 import BeautifulSoup

with open('day45/bs4-start/web.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

ancor_tags = soup.find_all(name='a')
#print(ancor_tags)

for tag in ancor_tags:
    print(tag.getText() + ' : ' + tag.get('href'))

heading = soup.find(name='h1', id='name')
print(heading)

company_url = soup.select_one(selector="p a")
print(company_url)