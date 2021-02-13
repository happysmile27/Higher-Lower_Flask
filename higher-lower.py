from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def title():
    return "<h1>Guess numbers of pandas between 0 and 9<h1>" \
           "<img src='https://media.giphy.com/media/gqDbzvWihXOtW/giphy.gif' width=200>"

rand = random.randint(0, 9)

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > rand:
        return "<h1 style='color: red'>Too high, try again<h1>" \
               "<img src='https://media.giphy.com/media/wbFiPNhOEVKkU/giphy.gif' width=500>"
    elif guess < rand:
        return "<h1 style='color: blue'>Too low, try again!<h1>" \
               "<img src='https://media.giphy.com/media/EatwJZRUIv41G/giphy.gif' width=500>"
    else:
        return "<h1 style='color: green'>You guess correctly<h1>" \
               "<img src='https://media.giphy.com/media/bEqrzkLVWC3bW/giphy.gif' width=500>"

if __name__ == '__main__':
    app.run(debug=True)