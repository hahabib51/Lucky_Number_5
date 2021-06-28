from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import random

app = Flask(__name__)
CORS(app)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=['POST'])
def get_lucky_num():
    """Get lucky num JSON response."""
    # Creating an empty dict for errors
    errors = {}

    # Grabbing the form values
    # name = request.form.get('name')
    # email = request.form.get('email')
    # year_num = request.form.get('year')
    # color = request.form.get('color')

    name = request.json['name']
    email = request.json['email']
    year_num = request.json['year']
    color = request.json['color']

    # Adding the individual errors to the dictionary
    if name is None:
        errors['name'] = ['This field is required.']

    if email is None:
        errors['email'] = ['This field is required.']

    try:
        if year_num is None:
            errors['year'] = ['This field is required.']
        elif (int(year_num) < 1900) or (int(year_num) > 2000):
            errors['year'] = [
                'Birth year must be between 1900 and 2000, inclusive.']
    except TypeError:
        errors['year'] = [
            'Birth year must be between 1900 and 2000, inclusive.']

    try:
        if color is None:
            errors['color'] = ['This field is required.']
        elif color not in ('red', 'green', 'orange', 'blue'):
            errors['color'] = [
                'Invalid value, must be one of: red, green, orange, blue.']
    except TypeError:
        errors['color'] = [
            'Invalid value, must be one of: red, green, orange, blue.']

    # Return errors if there are any
    if errors:
        return jsonify(errors=errors)

    # Numbers API integration
    base_url = 'http://numbersapi.com'

    num = {}
    year = {}

    # Creating the lucky number
    lucky_num = random.randint(1, 100)

    # Request the random fact
    num['fact'] = requests.get(f'{base_url}/{lucky_num}').text
    num['num'] = lucky_num

    year['fact'] = requests.get(f'{base_url}/{year_num}/year').text
    year['year'] = year_num

    return jsonify(num=num, year=year)