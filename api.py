from flask import Flask
import logging, os


app = Flask(__name__)

@app.route('/')
def ping():
    welcome = '''
    Hello, this is Apertium translate API. 
    An API to help you on translation application projects.
    You can ...
            '''
    return welcome

if __name__ == "__main__":
    app.run(debug=True)


