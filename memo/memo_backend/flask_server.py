from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

##서비스에 직접적으로

##url comment를 넘기는 api를 만드는 것
@app.route('/post', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    ##requests : import 패키지
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    article = {'url': url_receive, 'comment': comment_receive, 'image': url_image,
               'title': url_title, 'desc': url_description}

    ## dict 형태로 저장

    db.articles.insert_one(article)
    ##db중 articles 라는 콜렉션을 만들고 dict를 저장

    return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def listing():
    ##db에서 아티클즈를 가져와서 리스트 형태로 만듬
    result = list(db.articles.find({}, {'_id':0}))
    return jsonify({'result':'success', 'articles' : result})
##화면을 그리기 위한 응답, 데이터를 전달하기 위한 응답
##1 = render_template / 2 = jsonify

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
##플라스크가 돌아가게 하는 함수

