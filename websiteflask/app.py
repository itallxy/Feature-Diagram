from email import message
from multiprocessing import connection
import sqlite3

from flask import Flask, render_template,request
import os

currdir=os.path.dirname(os.path.abspath(__file__))

 

app = Flask(__name__)



@app.route('/user/<name>')
def user(name):
    return 'the name is: ' + name

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about', endpoint ='about')
def about():
    return render_template('about.html')

@app.route('/login', endpoint ='login')
def login():
    return render_template('login.html')

@app.route('/neww', endpoint ='neww')
def neww():
    return render_template('neww.html')


@app.route('/save',methods=["POST"])
def save():
    if request.method =='POST':
        jose=request.form.get('t1')
        nmid=request.form.get('idgraph')
        connection=sqlite3.connect("./featureDiagram.db")
        cursor=connection.cursor()
        q1="INSERT INTO FeatureDiagarm VALUES ('{N}','{P}')".format(N=nmid,P=jose)
        cursor.execute(q1)
        connection.commit()
        return render_template('neww.html')
    return render_template('neww.html',message="")

@app.route('/team', endpoint ='team')
def team():
    return render_template('team.html')



if __name__ == '__main__':
      app.run(debug=True)
    
