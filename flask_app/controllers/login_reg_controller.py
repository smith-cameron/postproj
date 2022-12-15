from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    #validate user input
    if user.User.validate_create(request.form):
        #secure the password via bcrypt
        print(request.form['password'])
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        #if valid save to db
        data ={
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        #store the user in session
        session['user_id'] = user.User.save(data)
        #redirect to /home
        return redirect('/wall')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = user.User.getByEmail(data)
    if user_in_db:
        #validate user input
        if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            #store the user in session
            session['user_id'] = user_in_db.id
            #redirect to /home
            return redirect("/wall")
    flash("Invalid Credentials", 'loginError')
    return redirect('/')

@app.route('/logout')
def logout():
    #clear session
    # print(session['user_id'])
    session.clear()
    # print(session['user_id'])
    #redirect to root route
    return redirect('/')