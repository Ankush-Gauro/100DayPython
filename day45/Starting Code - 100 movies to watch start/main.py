import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

movie = [name.getText() for name in soup.findAll(name='h3', class_='title')]
ordered_movie = movie[::-1]

with open('bestmovies.txt','w') as file:
    for i in range(len(ordered_movie)):
        if i == 58:
            file.write("59) E.T. The extra Terrestrial" + "\n")
        else:
            file.write(ordered_movie[i])
            file.write("\n")

