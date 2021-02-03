
from app_src import app
from flask import render_template
import json
import random

with open('./quiz_data/index.json') as f:
  data = json.load(f)

@app.route("/")
def index():
    return render_template("home.html",home="active")

@app.route("/about")
def about():
    return render_template("about.html",about="active")

@app.route("/archives")
def archive():
    return render_template("archives.html",archives="active")

@app.route("/question/<quiz_num>/<ques_num>")
def ques(quiz_num,ques_num):
    if(quiz_num in data): 
        with open(f'./quiz_data/{data[quiz_num]}') as f1:
            lo_data = json.load(f1)
        if(ques_num in lo_data.keys()):
            print("hi")
            return render_template("question.html",question_data=lo_data[ques_num], quiz_num=quiz_num, ques_num=ques_num, quiz_name=data[quiz_num])
        else :
            return "invalid 1"
    else:
        return "invalid 2"

@app.route("/question/<quiz_num>/<ques_num>/answer")
def ques_ans(quiz_num,ques_num):
    if(quiz_num in data): 
        with open(f'./quiz_data/{data[quiz_num]}') as f1:
            lo_data = json.load(f1)
        if(ques_num in lo_data.keys()):
            print("hi")
            return render_template("answer.html",question_data=lo_data[ques_num], quiz_num=quiz_num, ques_num=ques_num, quiz_name=data[quiz_num])
        else :
            return "invalid 1"
    else:
        return "invalid 2"

@app.route("/tags")
def tag_landing():
    rnd_top=random.choice(["mela","st","sp","ind","gen"]) # add biz back when it is non empty
    with open(f'./quiz_data/tagged/{rnd_top}.json') as f1:
        lo_data = json.load(f1)
    return render_template("tag.html",random=random.choice(lo_data),rnd_topic=rnd_top)

@app.route("/tags/<tag>")
def tag_page(tag):
    if tag in ["mela","st","sp","biz","ind","gen"]:
        with open(f'./quiz_data/tagged/{tag}.json') as f1:
            lo_data = json.load(f1)
        return render_template("actual_tag.html",TAG=tag,tag_data=lo_data,random=random.choice(lo_data))
    else:
        return "Invalid 1"
