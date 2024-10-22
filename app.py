import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World! This is a test flask 123123123'
if __name__ == '__main__':
    app.run(debug=True)
    print(os.environ['env_var1'])
    print(os.environ['env_var2'])