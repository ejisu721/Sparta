from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from bs4 import BeautifulSoup
import requests

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
    return render_template('index.html')

## 주문하기 API
@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give']  # 클라이언트로부터 url을 받는 부분
    number_receive = request.form['number_give']  # 클라이언트로부터 url을 받는 부분
    address_receive = request.form['address_give']  # 클라이언트로부터 url을 받는 부분
    phone_receive = request.form['phone_give']  # 클라이언트로부터 url을 받는 부분


    shopping = {'name': name_receive,
                'number': number_receive,
                'address': address_receive,
               'phone': phone_receive}

    db.shoppings.insert_one(shopping)

    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])
def listing():
    ##db에서 아티클즈를 가져와서 리스트 형태로 만듬
    result = list(db.shoppings.find({}, {'_id':0}))
    return jsonify({'result':'success', 'shoppings' : result})
##화면을 그리기 위한 응답, 데이터를 전달하기 위한 응답
##1 = render_template / 2 = jsonify

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)