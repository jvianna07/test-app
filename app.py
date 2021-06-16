from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return '<h1> It works fine!</h1>'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')