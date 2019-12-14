#coding:utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get('http://699pic.com/photo-0-0-complex-lateral-0-all-all-1-0-0-0-0-0-0-all-all.html')
print(r)
soup = BeautifulSoup(r.text,"html.parser")
all = soup.find_all(class_='lazy')
for i in all:
    try:
        url_jpg = (i['data-original'])
        name_jpg = i['title']
        print(name_jpg)
        r1 = requests.get(url_jpg)
        #print(r1)

        fp = open("E:\\img\\%s.jpg" % name_jpg, 'wb')
        fp.write(r1.content)
        fp.close()
    except:
        pass






