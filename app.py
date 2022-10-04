from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qatest.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    gender = db.Column(db.String)
    dateadd = db.Column(db.String)
    meals = db.relationship('Meals' ,backref='all_meals')

class Meals(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.ForeignKey('user.id'))
    breakfast = db.Column(db.String)
    lunch = db.Column(db.String)
    dinner = db.Column(db.String)
    snacks = db.Column(db.String)
    drinks = db.Column(db.String)
    workout = db.relationship('Workout' ,backref='all_workouts')

class Workout(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    meal = db.Column(db.ForeignKey('meals.id'))
    kickboxing = db.Column(db.String)
    boxing = db.Column(db.String)
    push_up = db.Column(db.String)
    pull_up = db.Column(db.String)
    meals = db.relationship('User' ,backref='all_users')
 
#db.create_all()

@app.route('/')

def index():
    return render_template("index.html")
    

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000) 
#