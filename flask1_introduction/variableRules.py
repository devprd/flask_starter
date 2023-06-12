from flask import Flask

app = Flask(__name__)


# Method 1
@app.route('/')
def welcome():
    return "Hello Guys"

# Method 2
@app.route('/reporter/<int:reporter_Id>')
def reporter(reporter_Id):
    return f'''<h2>This is the reporter {reporter_Id} page</h2><a href = '/'> Click Here to go back to Welcome page.</a>'''


app.run(debug=True)