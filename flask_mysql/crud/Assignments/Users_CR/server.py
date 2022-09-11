from flask import Flask, render_template, session, request, redirect
from user import User
app = Flask(__name__)
# import the class from user.py

@app.route("/")
def index():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    print(all_users)
    return render_template('Read.html', all_users = all_users )


#Go to Create user Page
@app.route('/Create')
def create_page():
    return render_template("Create.html")

#Create user
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



if __name__ == "__main__":
    app.run(debug=True)