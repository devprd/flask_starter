from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h2>Welcome to this Page.</h2>"

@app.route('/reporter/<int:reporter_Id>')
def reporter(reporter_Id):
    return f'''<h2> Reporter {reporter_Id} Page </h2><a href = '/'>Go back to Welcome Page</a>'''
    
@app.route('/article/<name>')
def article(name):
    return f'''<h2> Article {name.replace('-',' ').title()} page </h2>'''


app.run()