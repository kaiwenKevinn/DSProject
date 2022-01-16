import os.path

from flask import Flask, request, session, jsonify
from flask_cors import CORS
from NLPHelper import NLPHelper
import time
app = Flask(__name__)

app.config["SECRET_KEY"] = "renyizifuchuan"

CORS(app, supports_credentials=True)


# @app.before_first_request
# def init():


@app.route("/download", methods=['POST', 'GET'])
def save():

    param=time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    print(param)
    f = request.files["file"]
    basepath = os.path.dirname(__file__)  # 当前文件所在的路径
    print(basepath)
    downloadpath = basepath + "\\FILES\\test%s.txt" % param
    print(downloadpath)
    session["path"]=downloadpath
    f.save(downloadpath)

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
    causes = list(causes)
    MyDict = {
        "name": name,
        "ethnicity": ethnicity,
        "birthplace": birthplace,
        "gender": gender,
        "courts": courts,
        "causes": causes
    }

    return MyDict
