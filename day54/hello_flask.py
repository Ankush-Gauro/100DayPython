from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello world"

@app.route('/bye')
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()