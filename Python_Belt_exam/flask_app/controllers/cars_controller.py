from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.car_model import Car

@app.route('/cars/new')
def new_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("cars_new.html")

@app.route('/cars/create', methods=['POST'])
def add_car():
    if 'user_id' not in session:
        return redirect ('/')
    if not Car.validator(request.form):
        return redirect('/cars/new')
    data = {
        **request.form,
        'user_id':session['user_id']
    }
    id = Car.create(data)
    return redirect ('/welcome')
    # (f'/cars/{id}')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
    if 'user_id' not in session:
        return redirect ('/')
    car = Car.get_by_id({'id':id})
    Car.delete({'id':id})
    return redirect('/welcome')

@app.route("/cars/<int:id>/edit")
def edit_car_form(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    if not int(session['user_id']) ==car.user_id:
        flash("Hey these cars are still for sale, get your paws off!!!")
        return redirect ('/welcome')
    car = Car.get_by_id({'id':id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = Car.get_by_id(user_data)
    return render_template("cars_edit.html", car = car, logged_user = logged_user)

@app.route('/cars/<int:id>/update', methods = ['POST'])
def update_car(id):
    if 'user_id' not in session:
        return redirect('/')
    car = Car.get_by_id({'id':id})
    if not int(session['user_id']) ==car.user_id:
        flash("Hey these are precious recipes, get your paws off!!!")
        return redirect ('/welcome')
    if not Car.validator(request.form):
        return redirect(f"/cars/{id}/edit")
    data = {
        **request.form,
        'id':id
    }
    Car.update(data)
    return redirect('/welcome')

@app.route("/cars/<int:id>")
def show_cars(id):
    car = Car.get_by_id({'id':id})
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template("cars_one.html", car = car, logged_user = logged_user)