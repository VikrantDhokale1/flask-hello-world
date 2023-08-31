# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from your Python app!"

if _name_ == '__main__':
    app.run(host='0.0.0.0', port=8000)
