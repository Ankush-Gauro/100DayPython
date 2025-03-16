from flask import Flask
app = Flask(__name__)

def bold_wrapper(function):
    def make_bold():
        return f"<b>{function()}</b>"
    return make_bold

def emphesis_wrapper(function):
    def make_emphesis():
        return f"<em>{function()}</em>"
    return make_emphesis

def underline_wrapper(function):
    def make_underline():
        return f"<u>{function()}</u>"
    return make_underline




@app.route('/')
@bold_wrapper
@emphesis_wrapper
def helloworld():
    return "Hello world"

@app.route('/bye')
def say_bye():
    return "<h1 style='text-align: center'>Bye</h1>" \
    "<p>This is a paragraph</p>" \
    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWJkemM5dmtjNGZ0cmZ4Zjh2ZTlpY3B6dzg3ZHl2MHlvMnl1YXdxNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MDJ9IbxxvDUQM/giphy.gif'>"

@app.route('/<name>/<num>')
def say_name(name,num):
    return f"Hello there {name}, you are {num} years old"

if __name__ == "__main__":
    app.run(debug=True)