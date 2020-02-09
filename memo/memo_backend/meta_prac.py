import requests ##접속 및 요청
from bs4 import BeautifulSoup ##HTML을 편하게 분석

url = 'https://platum.kr/archives/120958'
## 크롤링 대상

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
##메타데이터의 헤더
data = requests.get(url,headers=headers)
##리퀘스트 라이브러리 변수, get 타입 요청

soup = BeautifulSoup(data.text, 'html.parser')
##응답의 텍스트를 갖고 오겠다, html 파서를 이용해서 html로 변형해줘

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

print(url_image, url_title, url_description)