from app import app
from flask import render_template, flash, redirect
from flask import request
from flask import url_for
from flask import jsonify

#routes – URLs where a flask app accepts requests
from app.forms import LoginForm

@app.route("/index", methods=['GET','POST'])
@app.route("/login2", methods=['GET','POST'])
@app.route('/login', methods=['GET', 'POST'])
#@app.route("/lkremer", methods=['GET','POST'])

@app.route('/login', methods=['GET', 'POST'])
def login():    
    form = LoginForm()    
    if request.method == 'POST':        
       if form.validate_on_submit():            
          flash('Welcome user {}! You opted for remember_me={}'.format(form.username.data, form.remember_me.data))            
          return redirect("/lkremer")    
    else:        
       if request.args:
          flash('GET method now allowed for login!')        
          # else:        
          #     flash('No data in request!')    
    return render_template('login.html', title='Sign In', form=form)
@app.route('/index3')
@app.route('/')
@app.route('/index')
#a view function – route handler
def index():
    user = {'username': 'lkremer'}
    classes = [ {'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},                     {'classInfo': {'code': 'CSC184', 'title': 'Python Programming'}, 'instructor': 'Evan Noynaert'}]    
    return render_template('index.html', title='Home', user=user, classes=classes) 

@app.route('/lkremer')
def lkremer():
    user = {'username': 'lkremer'}
    return render_template('lkremer.html', title='lkremer')

@app.route('/json')
def jsonTest():
    instructor = {
        "username": "lkremer",
        "role": "student",
        "uid": 11,
        "name": {
            "firstname": "Kremer",
            "lastname": "Lilly"
        }
    }

    return jsonify(instructor)

