
from app_src import app
from flask import render_template
import json

with open('./quiz_data/index.json') as f:
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
    if(quiz_num in data): 
        print(data[quiz_num])
        with open(f'./quiz_data/{data[quiz_num]}') as f1:
            lo_data = json.load(f1)
        if(("Q"+ques_num ) in lo_data):
            return render_template("question.html",question_url=lo_data["Q"+ques_num]["q_url"],answer_url=lo_data["Q"+ques_num]["a_url"])
        else :
            return "invalid"
        
    else:
        return "invalid"

@app.route("/questionview/<ques_num>")
def quesview(ques_num):
    return render_template("question.html",question_url=data["Q"+ques_num]["q_url"])