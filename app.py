from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a test flask app and i made some changes :D 2nd time now'

if __name__ == '__main__':
    app.run(debug=True)