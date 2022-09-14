from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User

bcrypt = Bcrypt (app)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/users/register', methods=['POST'])
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
    return render_template ('welcome.html')

@app.route('/users/login', methods=['POST'])
def login():
#FIRST, see if the username provided exists in database
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)
    #if user is not registered
    if not user_in_db:
        flash ('Invalid login info', 'log')
        return redirect('/')
    #if the user exists, check the password
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ('Invalid login info', 'log')
        return redirect('/')
    #log user in
    session['user_id'] = user_in_db.id
    return redirect ('/welcome')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect ('/')