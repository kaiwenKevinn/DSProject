from flask import Flask, request, g, jsonify
from flask_cors import CORS
from NLPHelper import NLPHelper

app = Flask(__name__)

CORS(app, supports_credentials=True)


# @app.before_first_request
# def initNlp():


@app.route("/download",methods=['POST' , 'GET'])
def save():
    print("hello")
    return "helloWorld"


@app.route("/search/")
def exp():
    # print(request.args.get('ID'))
    # print(request.form)
    # 可以加参数（文件名）
    nlp = NLPHelper()
    nlp.process()
    # g.nlp = nlp
    name = nlp.info['name']
    ethnicity = nlp.info['ethnicity']
    birthplace = nlp.info['birthplace']
    gender = nlp.info['gender']
    courts = nlp.info['courts']
    causes = nlp.info['causes']
    causes =list (causes)
    MyDict = {
        "name": name,
        "ethnicity": ethnicity,
        "birthplace": birthplace,
        "gender": gender,
        "courts": courts,
        "causes": causes
    }

    return MyDict
