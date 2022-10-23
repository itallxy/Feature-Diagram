from flask import Flask, render_template
import sqlite3
 
conn = sqlite3.connect('mydb.db')
print ("Opened database successfully")
 

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

@app.route('/team', endpoint ='team')
def team():
    return render_template('team.html')



if __name__ == '__main__':
      app.run(debug=True)
    
