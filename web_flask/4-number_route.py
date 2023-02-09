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

=======
@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """returns HBNB"""
        return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
        """display “C ” followed by the value of the text variable"""
        return 'C ' + text.replace('_', ' ')
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
<<<<<<< HEAD
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

=======
        """display “Python ”, followed by the value of the text variable"""
        return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
        """display “n is a number” only if n is an integer"""
        return "{:d} is a number".format(n)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
