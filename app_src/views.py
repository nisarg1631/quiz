from app_src import app
from flask import render_template
import json

with open('./quiz_data/new_year.json') as f:
  data = json.load(f)

@app.route("/")
def index():
    return "Insert Welcome Page Here"

@app.route("/about")
def about():
    return "Insert About Page Here"

@app.route("/question/<quiz_num>/<ques_num>")
def ques(quiz_num,ques_num):
    print(quiz_num,ques_num)
    print(data['Q1'])
    return render_template("question.html",question_url=data["Q1"]["q_url"])

@app.route("/questionview/<ques_num>")
def quesview(ques_num):
    return render_template("question.html",question_url=data["Q"+ques_num]["q_url"])