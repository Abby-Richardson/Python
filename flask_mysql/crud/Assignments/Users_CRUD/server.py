from flask import Flask, render_template, session, request, redirect
from user import User
app = Flask(__name__)
# import the class from user.py

#ALL USERS PAGE
@app.route("/")
def index():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    print(all_users)
    return render_template('Read.html', all_users = all_users )



#GO TO CREAT USER PAGE
@app.route('/Create')
def create_page():
    return render_template("Create.html")

#CREATE USER
@app.route("/Create/user", methods = ['POST'])
def create_user():
    # # First we make a data dictionary from our request.form coming from our template.
    # # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # # # We pass the data dictionary into the save method from the User class.
    User.create(data)
    return redirect ('/')

#SHOW USER
@app.route('/users/<int:id>')
def show_user(id):
    data ={
        'id':id
    }
    one_user = User.get_one(data)
    return render_template ('user_show.html', one_user = one_user)

#UPDATE USER
@app.route('/users/<int:id>/edit')
def edit_user (id):
    data = {
        'id':id
    }

    this_user = User.get_one(data)
    return render_template ("user_edit.html", this_user = this_user)

@app.route('/users/<int:id>/update', methods = ['POST'])
def update_user (id):
    data = {
        **request.form,
        'id':id
    }
    User.update(data)
    return redirect ('/')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect ('/')



if __name__ == "__main__":
    app.run(debug=True)