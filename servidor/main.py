# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')


@app.route(r'/add', methods=['GET','POST'])
def add_contact():

    if request.form:
        print("hola")
        print(request.form.get('name'))
        print(request.form.get('phone'))
        print(request.form.get('email'))
    else:
        print("adios")
        print('hola')

    return render_template('add_contact.html')
#@app.route('/')
#def hello_world():
#    return 'Hola mundo.'

if __name__ == "__main__":
    app.run()