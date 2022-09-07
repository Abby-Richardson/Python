from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secretssssss"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process_form():
    print (request.form)
    session['name'] = request.form ['name']
    session['location'] = request.form ['location']
    session['language'] = request.form ['language']
    session['comment_box'] = request.form ['comment_box']
    return redirect('/result')


@app.route('/result')
def input_results():
    return render_template("result.html")






if __name__=="__main__": 
    app.run(debug=True)