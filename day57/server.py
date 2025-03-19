from flask import Flask, render_template
import random
from datetime import date
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    random_num = random.randint(1,9)
    today_date = date.today()
    return render_template('index.html', num=random_num, year = today_date.year)

@app.route('/guess/<name>')
def guess(name):
    gen_url = f"https://api.genderize.io?name={name}"
    gen_response = requests.get(gen_url)
    gen_data = gen_response.json()
    gender = gen_data['gender']
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('render.html', p_name = name, p_gender = gender, p_age = age)

@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)