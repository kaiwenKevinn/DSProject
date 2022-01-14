from flask import Flask,request,g
from flask_cors import CORS
from NLPHelper import NLPHelper

app = Flask(__name__)

CORS(app, supports_credentials=True)

# @app.before_first_request
# def initNlp():




@app.route("/")
def init():
    print("hello")
    return "helloWorld"


@app.route("/user/")
def exp():
    # print(request.args.get('ID'))
    # print(request.form)
    # 可以加参数（文件名）
    nlp = NLPHelper()
    nlp.process()
    # g.nlp = nlp
    name = nlp.info['name']
    type(name)
    print(name)
    return "200"