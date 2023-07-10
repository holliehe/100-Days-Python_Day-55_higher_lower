from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def guess():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" width="480"></img>'

rand_int = random.randint(0,9)
print(rand_int)
@app.route('/<int:number>')
def lower_higher(number):
    if number<rand_int:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               "<img src='https://media.giphy.com/media/lFfLINS1MkZs4/giphy.gif' width='480'></img>"
    elif number>rand_int:
        return '<h1 style="color: blue;">Too high, try again!</h1>' \
               "<img src='https://media.giphy.com/media/5gXYzsVBmjIsw/giphy.gif' width='480'></img>"
    else:
        return '<h1 style="color: purple;">You found me!</h1>' \
               "<img src='https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif' width='480'></img>"

if __name__ == '__main__':
    app.run(debug=True)