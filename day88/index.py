from flask import Flask, render_template, redirect, url_for, request

import csv



app = Flask(__name__)



@app.route('/')

def home():

    return render_template('index.html')



@app.route('/add', methods=["GET", "POST"])

def add_cafe():

    if request.method == "POST":

        data = request.form.to_dict()

        with open('cafes.csv', mode='a', encoding='utf-8', newline='') as file:

            writer = csv.writer(file)

            writer.writerow(data.values())

        return redirect(url_for('cafes'))

    return render_template('add.html')



@app.route('/cafes')

def cafes():

    with open('cafes.csv', newline='', encoding='utf-8') as csv_file:

        csv_data = list(csv.reader(csv_file))

        headers = csv_data[0]

        rows = csv_data[1:]

    return render_template('cafes.html', headers=headers, rows=rows)



if __name__ == '__main__':

    app.run(debug=True)