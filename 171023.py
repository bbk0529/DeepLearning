
#실습 예제 
#네이버 포털의 뉴스기사를 크롤링하는 예제를 Python으로 만들어서 제출하세요.


from bs4 import BeautifulSoup
import urllib.request
import re

output='result.txt'
url='http://news.naver.com/main/read.nhn?oid=001&sid1=102&aid=0009627114&mid=shm&viewType=pc&mode=LSD&nh=20171023133343'

def get_text(URL):
    sourcecode=urllib.request.urlopen(URL)
    soup=BeautifulSoup(sourcecode, 'lxml', from_encoding='utf-8')
    content=''
    for component in soup.find_all('div', id='articleBodyContents'):
            text=str(component.find_all(text=True))
            text=re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', text )
            text=re.sub('[a-zA-Z]','', text)
            content+=text
    return content

def write_file(content, filename) : 
    f=open(filename, 'w', encoding='utf-8')
    f.write(content)
    f.close()

#실행부분    
content=get_text(url)  
write_file(content, 't.txt')