from flask import Flask, render_template, redirect, url_for,request,jsonify
from flask import make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/index")
def home():
    # return render_template('frontend.html')
    return "hi"

@app.route('/login', methods=['GET', 'POST'])
def login():
   message = None
   if request.method == 'POST':
        datafromjs = request.form['mydata']
        print(datafromjs)
        result = "return this"
        # resp = make_response('{"response": '+result+'}')
        # resp.headers['Content-Type'] = "application/json"
        # resp.headers['Access-Control-Allow-Origin'] = "*"
        return jsonify({'result':'YES'})
        # return render_template('login.html', message='')

if __name__ == "__main__":
    app.run(debug = True)