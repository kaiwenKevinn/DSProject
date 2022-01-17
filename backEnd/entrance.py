import json
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
location=[""]

@app.route("/download/upload", methods=['POST', 'GET'])
def save():

    param=time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    # print(param)
    f = request.files["file"]
    basepath = os.path.dirname(__file__)  # 当前文件所在的路径

    downloadpath = basepath + "\\FILES\\上传的文件%s.txt" % param

    f.save(downloadpath)
    global location
    location[0]= downloadpath
    # print("上传文件时",location)
    # session["dizhi"]=downloadpath
    f.close()

    return "200"

@app.route("/download/annotation",methods=['POST','GET'])
def saveAnnotation():
    param = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    basepath = os.path.dirname(__file__)  # 当前文件所在的路径
    downloadpath = basepath + "\\FILES\\标注%s.json" % param

    annotation=request.data.decode()
    annotation=annotation[annotation.index(':')+1:]
    annotation=annotation[0:len(annotation)-1]
    mydict=json.loads(annotation)

    # print(annotation)
    # print("mydict",type(mydict))
    with open(downloadpath,"w",encoding='utf-8') as f:
        json.dump(mydict,f,indent=4,ensure_ascii=False)

    return "200"

@app.route("/search/text",methods=["GET","POST"])
def exp():
    param = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    basepath = os.path.dirname(__file__)
    downloadpath = basepath + "\\FILES\\裁判文书%s.txt" % param

    userInput=request.data.decode()
    userInput=userInput.lstrip("{")
    userInput=userInput.rstrip("}")
    dealing=userInput.split(":")
    # print(userInput)
    dealing[1]=dealing[1].replace("\\n","~")
    print(dealing[1])
    length=len(dealing[1])
    f = open(downloadpath,"w",encoding='utf-8')
    for i in range(0,length,1):
        if dealing[1][i]=='~':
            f.write('\n')
        else:
            f.write(dealing[1][i])

    f.close()

    return diaoYong(downloadpath)


@app.route("/analyze/upload",methods=['GET','POST'])
def analyze():
    global location
    # print("要调用了",location[0])
    return diaoYong(location[0])

def diaoYong(fileName):
    # print(fileName)
    nlp = NLPHelper(fileName)
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