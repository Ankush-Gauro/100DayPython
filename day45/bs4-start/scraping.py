from bs4 import BeautifulSoup
import requests

stat_response = requests.get('https://appbrewery.github.io/news.ycombinator.com')

stat_soup = BeautifulSoup(stat_response.text, 'html.parser')

titles = [title.getText() for title in stat_soup.find_all(name='a', class_ = 'storylink')]
links = [title.get('href') for title in stat_soup.find_all(name='a', class_ = 'storylink')]
upvotes = []
upvote = stat_soup.find_all(name='span', class_ = 'score')
for vote in upvote:
    up_count = int(vote.getText().split()[0])
    upvotes.append(up_count)



highest_upvote_index = upvotes.index(max(upvotes))
print('Highest Upvote Title: ', titles[highest_upvote_index], 'Link: ', links[highest_upvote_index], 'Upvote Count: ', max(upvotes))
