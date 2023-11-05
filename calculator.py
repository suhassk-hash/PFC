from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/', methods=["POST","GET"])
def index():
    if request.method=="POST":
      number_1=request.form['number1']
      number_2=request.form['number1']
      return (number_1,number_2)
    else:
      return render_template('index.html')
@app.route('/add', methods=["POST","GET"])
def add():
    if request.method=="POST":
      number_1=request.form['number1']
      number_2=request.form['number1']
      y=int(number_1)+int(number_2)
      return render_template('index.html',result=y)
    else:
      return render_template('index.html')
@app.route('/sub', methods=["POST","GET"])
def sub():
    if request.method=="POST":
      number_1=request.form['number1']
      number_2=request.form['number1']
      y=int(number_1)-int(number_2)
      return render_template('index.html',result=y)
    else:
      return render_template('index.html')