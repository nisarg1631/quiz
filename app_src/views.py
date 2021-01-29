
from app_src import app
from flask import render_template
import json

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
            return render_template("question.html",question_data=lo_data[ques_num])
        else :
            return "invalid 1"
    else:
        return "invalid 2"

@app.route("/tags")
def tag_landing():
    return render_template("tag.html")

@app.route("/tags/<tag>")
def tag_page(tag):
    if tag in ["mela","st","sp","biz","ind","gen"]:
        with open(f'./quiz_data/tagged/{tag}.json') as f1:
            lo_data = json.load(f1)
        return render_template("actual_tag.html",TAG=tag,tag_data=lo_data)
    else:
        return "Invalid 1"
