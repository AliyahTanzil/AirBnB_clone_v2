#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
        """returns Hello HBNB!"""
        return 'Hello HBNB!'

<<<<<<< HEAD

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """returns HBNB"""
        return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
        """display “C ” followed by the value of the text variable"""
        return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
