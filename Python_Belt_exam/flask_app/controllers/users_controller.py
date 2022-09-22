import re
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.car_model import Car

bcrypt = Bcrypt (app)

@app.route('/')
def index():
    return render_template('index.html')


#checking for validation/creating user/directing to welcome dashboard
@app.route('/users/register', methods = ['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_cars = Car.get_all()
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template('dashboard.html', all_cars = all_cars, logged_user = logged_user)

@app.route('/users/login', methods = ['POST'])
def login():
    #check if the user is in database
    data = {'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user is not registered, redirect to register
    if not user_in_db:
        flash("Invalid login info", "log")
        return redirect ('/')
    #if the user exists, check that password matches
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ("Invalid login info", 'log')
        return redirect ('/')
    #log user in
    session['user_id'] = user_in_db.id
    return redirect('/welcome')


@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')