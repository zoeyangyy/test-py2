# coding=utf-8
import requests
import json
from bs4 import BeautifulSoup


def json_version():
    try:
        web=requests.get('http://www.a-hospital.com/w/%E7%9A%AE%E8%82%A4%E7%96%BE%E7%97%85%E6%9F%A5%E8%AF%A2')
        web.encoding='utf-8'
        soup = BeautifulSoup(web.text, 'html.parser')

        table = soup.find(id="bodyContent").find_all('ul', recursive=False)[1]

        list1 = []
        for li in table.find_all('li'):
            for a in li.find_all('a', recursive=False):
                dict1={}
                dict1['name']=a.text
                dict1['href']=a['href']
                try:
                    # time.sleep(1+random.random())
                    subweb=requests.get('http://www.a-hospital.com'+dict1['href'])
                    subsoup = BeautifulSoup(subweb.text, "html.parser")
                    dict1['description']=subsoup.find(id='bodyContent').find('p', recursive=False, text=True).text

                except:
                    dict1['description']='not find'
                    pass
                list1.append(dict1)

        file = open('./disease/crawler.txt', 'w')
        for i in list1:
            file.write(json.dumps(i, ensure_ascii=False, encoding='utf-8'))
            file.write("\n")
        file.close()

    except:
        print 'web cannot open'


def text_version():
    try:
        web=requests.get('http://www.yixue.com/%E5%86%85%E7%A7%91%E7%96%BE%E7%97%85')
        web.encoding='utf-8'
        soup = BeautifulSoup(web.text, "html.parser")

        table = soup.find(id='mw-content-text').find('ul', recursive=False)

        list1 = []
        for li in table.find_all('li'):
            for a in li.find_all('a', recursive=False):
                dict1 = {}
                dict1['name']=a.text
                try:
                    # time.sleep(1+random.random())
                    subweb=requests.get('http://www.yixue.com'+a['href'])
                    subsoup = BeautifulSoup(subweb.text, "html.parser")
                    des = ''
                    for p in subsoup.find(id='mw-content-text').find_all('p', recursive=False):
                        des += p.text
                    dict1['description']=des
                except:
                    dict1['description']='not find'
                    pass
                list1.append(dict1)

        file = open('crawler.txt', 'w')
        for i in list1:
            file.write(json.dumps(i, ensure_ascii=False, encoding='utf-8'))
            file.write("\n")
        file.close()

    except:
        print 'web cannot open'

text_version()
