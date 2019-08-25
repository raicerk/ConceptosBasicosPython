from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hola():
    return render_template('index.html')
#@app.route('/')
#def hello_world():
#    return 'Hola mundo.'

if __name__ == "__main__":
    app.run()