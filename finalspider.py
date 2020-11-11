import time
from requests_html import HTMLSession
session = HTMLSession()
headers = {
            'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
            'Host': 'movie.douban.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'Cookie': 'douban-fav-remind=1; gr_user_id=53a845ca-6028-422c-af92-b052e92ea2e3; _vwo_uuid_v2=D3B6764D7D760E8FCED537E3A6DFB0830|4b3941a07458591fccca9de93b9c255a; ll="108304"; viewed="4199509_1102235_26834083_24089577"; bid=a6b0vXZ6Rho; __yadk_uid=3d7o95GjbI6Wh4fDapznDZzxVuZ6MSuN; __utmz=30149280.1604926826.30.26.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1604926849.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_doumail_num=0; ct=y; __utmc=30149280; __utmc=223695111; __gads=ID=2a98f9cef35a429d:T=1605003836:S=ALNI_MYTPOslDNtFJ-wPL5pXXPfomC-ypw; __utmv=30149280.15372; __utma=30149280.538427823.1566537209.1605002753.1605006314.35; __utmb=30149280.1.10.1605006314; __utma=223695111.1834725759.1603852291.1605002850.1605006579.7; __utmb=223695111.0.10.1605006579; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1605006579%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; push_noty_num=0; dbcl2="183017563:uYqIKVSlcS4"; ck=bSTg; _pk_id.100001.4cf6=bd66e5bff8289219.1603852290.7.1605010058.1605004334.'
        }
plSelectList = []
for i in range(1, 21):
    plSelectList.append('#comments > div:nth-child(' + str(i) + ') > div.comment > p > span')
with open('plurl.txt','r') as f:
    plUrl = f.readlines()

plUrls = []
for url in plUrl:
    plUrls.append(url[:-1])
# print(plUrls[9999])
i = 6875
for url in plUrls[6875:]:
    print(url)
    response = session.get(url, headers=headers)
    pls = []
    for s in plSelectList:
        content = response.html.find(s)
        pls.append(content[0].text)
    f = open("pl.txt", "a+")
    for pl in pls:
        f.write(pl + '\n')
    f.close()
    i = i + 1
    print('--------------------------------------' + '第' + str(i) + '个页面爬取完毕' + '-------------------------------------')
    time.sleep(2)
