__author__ = 'Administrator'


import urllib2
import BeautifulSoup
import re

query = 'On+random+graph'
url = 'http://wenku.baidu.com/view/15a9a5b5cc22bcd126ff0c78.html'

header = {'Host' : 'wenku.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip,deflate,sdch',
    'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Connection':'keep-alive'}

req = urllib2.Request(url,headers=header)
con = urllib2.urlopen(req)

doc = con.read()

soup = BeautifulSoup.BeautifulSoup(doc)

paper_name = soup.html.body.find('h3',{'class' : 'gs_rt'}).text
paper_name = re.sub(r'\[.*\]', '', paper_name)
paper_author = soup.html.body.find('div', {'class' : 'gs_a'}).text
paper_desc = soup.html.body.find('div', {'class':'gs_rs'}).text
temp_str = soup.html.body.find('div',{'class':'gs_fl'}).text
temp_re = re.match(r'[A-Za-z\s]+(\d*)[A-Za-z\s]+(\d*)',temp_str)

citeTimes = temp_re.group(1)

versionNum = temp_re.group(2)

if citeTimes == '':
    citeTimes = '0'
if versionNum == '':
    versionNum = '0'

citedPaper_href = soup.html.body.find('div',{'class':'gs_fl'}).a.attrs[0][1]

print paper_name+'#'+paper_author+'#'+paper_desc


con.close()