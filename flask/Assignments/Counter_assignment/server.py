from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


# our index route will handle rendering our form
@app.route('/')
def visits_counter():
    if 'visits' in session:
        session ['visits'] +=1      #reading and updating session
    else:
        session['visits'] = 1       #setting session data
    return render_template("index.html")



@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
