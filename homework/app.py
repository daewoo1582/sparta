from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017) 
db = client.dbsparta                      

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework_4.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    ad_receive = request.form['ad_give']
    budget_receive = request.form['budget_give']
    email_receive = request.form['email_give']
    number_receive = request.form['number_give']

    doc = {
        'name':name_receive,
        'ad':ad_receive,
        'budget':budget_receive,
        'email':email_receive,
        'number':number_receive
    }
    db.homework4.insert_one(doc)

    return jsonify({'result':'success', 'msg': '추월차선 마케팅에 오르신걸 환영합니다!'})


@app.route('/customer', methods=['GET'])
def read_reviews():

    Customers = list(db.homework4.find({},{'_id':0}))

    return jsonify({'result':'success', 'client': Customers})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)