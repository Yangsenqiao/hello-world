import urllib,urllib.request
from bs4 import BeautifulSoup
key={}
key['s']='热爱'
keyword=urllib.parse.urlencode(key)
print('URL 请求参数字符为：')
print(keyword)
myurl='https://www.fundiving.com/?'
myaddr=myurl+keyword
htmsrc=urllib.request.urlopen(myaddr).read()
htmsrc=htmsrc.decode('UTF-8')
mysoup=BeautifulSoup(htmsrc,'lxml')
mydata=mysoup.select('#wrapper>div>div>div>div>selection')
print('搜索结果：')
print(mydata)