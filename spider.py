import json
from requests_html import HTMLSession
session = HTMLSession()
data ={
    'ck': '',
    'remember': False,
    'name': '15572459088',
    'password': 'db123456',
    'ticket': ''
}
headers = {
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
            'Host': 'accounts.douban.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

session = HTMLSession()

r = session.get('https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=500&page_start=0')
res = r.json()
print(res)
print(res['subjects'])
lists = res['subjects']

movies = []
for list in lists:
    movies.append(list['url'])
print(list)
print(len(list))
f = open("movies2.txt", "w")
for movie in movies:
    f.write(movie + '\n')
f.close()

