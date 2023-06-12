from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1> Hello Everyone </h1>"

@app.route('/reporter')
def reporter():
    return "<h2>reporter bio</h2><a href='/'>Return to welcome page</a>"

app.run()