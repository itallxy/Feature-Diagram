from email import message
from multiprocessing import connection
import sqlite3

from flask import Flask, render_template,request,jsonify
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
    return render_template('neww.html')

@app.route('/open',methods=["GET"])
def open():
    if request.method =='GET':
        connection=sqlite3.connect("./featureDiagram.db")
        cursor=connection.cursor()
        q2="SELECT * FROM FeatureDiagarm"
        res=cursor.execute(q2)
        res=res.fetchall()
        #print(res["ID"])
        return render_template('open.html',diagrams=res)
    return render_template('neww.html')
@app.route('/drow',methods=["POST"])
def drow():
    if request.method =='POST':
        jose=request.form.get('TEx')
        print(jose)
        connection=sqlite3.connect("./featureDiagram.db")
        cursor=connection.cursor()
        q2="SELECT JSON_VALUE FROM FeatureDiagarm where ID ={N}".format(N=jose)
        res=cursor.execute(q2)

        res=res.fetchall()
        cont={}
        rel=[]
       # for ress in res :
        print(res[0][0])
        #cont={'class':res[0],'nodeDataArray':res[1],'linkDataArray':res[2]}
        #rel.append(cont)
        
        #print(jsonify(rel))
        return render_template('neww.html',diagrams=res[0][0])

@app.route('/team', endpoint ='team')
def team():
    return render_template('team.html')



if __name__ == '__main__':
      app.run(debug=True)
    
