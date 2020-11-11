from requests_html import HTMLSession

session = HTMLSession()
data = {
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

with open('movies2.txt', 'r') as f:
    movies = f.readlines()

# top250 电影链接读取
urls = []
for movie in movies:
    urls.append(movie[:-1])

# 评论页面链接获取
plUrls = []
for url in urls:
    for i in range(0, 20):
        plUrls.append(url + 'comments?start=' + str(i * 2) + '0&limit=20&status=P&sort=new_score')
print(plUrls)
print(len(plUrls))  # 1w个评论页面
f = open("plurl.txt", "w")
for url in plUrls:
    f.write(url + '\n')
f.close()
