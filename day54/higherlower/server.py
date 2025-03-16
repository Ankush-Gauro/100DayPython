from flask import Flask
from random import randint

random_num = randint(1,9)

app = Flask(__name__)

@app.route('/')
def intro():
    return "<h1 style='text-align: center'><b>Choose a number between 1 and 10</b></h1>" \
    "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWJkemM5dmtjNGZ0cmZ4Zjh2ZTlpY3B6dzg3ZHl2MHlvMnl1YXdxNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/CjmvTCZf2U3p09Cn0h/200.webp'>"

@app.route('/<int:guess>')
def game(guess):
    if guess > random_num:
        return "<h1 style='text-align: center; color: red'><b>Number too high</b></h1>" \
    "<img src='https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif?cid=790b7611ibdzc9vkc4ftrfxf8ve9icpzw87dyv0yo2yuawq5&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif guess < random_num:
        return "<h1 style='text-align: center; color: yellow'><b>Number too low</b></h1>" \
    "<img src='https://media.giphy.com/media/hzBc3HCFc0icM/giphy.gif?cid=790b7611ibdzc9vkc4ftrfxf8ve9icpzw87dyv0yo2yuawq5&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    else:
        return "<h1 style='text-align: center; color: green'><b>You got it!!</b></h1>" \
    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWJkemM5dmtjNGZ0cmZ4Zjh2ZTlpY3B6dzg3ZHl2MHlvMnl1YXdxNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MDJ9IbxxvDUQM/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)