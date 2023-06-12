from flask import Flask

# Flask class instantiation
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():

    return "Hello World"

app.run()



