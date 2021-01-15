from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Python Web'

@app.route('/about')
def about():
    return 'about page'

@app.route('/login')
def login():
    return 'underconstruction!'


app.run()
