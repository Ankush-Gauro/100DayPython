import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.audible.com/search?keywords=book&node=18573211011"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('li', class_='bc-list-item')

books = []

for item in results:
    title_tag = item.find('h3', class_='bc-heading')
    author_tag = item.find('li', class_='authorLabel')
    length_tag = item.find('li', class_='runtimeLabel')

    title = title_tag.text.strip() if title_tag else 'N/A'
    author = author_tag.text.strip().replace("By: ", "") if author_tag else 'N/A'
    length = length_tag.text.strip().replace("Length: ", "") if length_tag else 'N/A'

    books.append([title, author, length])

# Save to CSV
with open('audible_books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Author', 'Length'])
    writer.writerows(books)

print("Saved to audible_books.csv")