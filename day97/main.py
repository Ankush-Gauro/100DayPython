from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
import stripe
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)

# Stripe setup
stripe.api_key = 'your_stripe_secret_key'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)  # in cents
    image = db.Column(db.String(300))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.query.get(product_id)
        if product:
            subtotal = product.price * quantity
            items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
            total += subtotal
    return render_template('cart.html', items=items, total=total)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout')
@login_required
def checkout():
    cart = session.get('cart', {})
    line_items = []
    for product_id, quantity in cart.items():
        product = Product.query.get(product_id)
        if product:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': product.name},
                    'unit_amount': product.price,
                },
                'quantity': quantity,
            })

    session_stripe = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('cart', _external=True)
    )

    return redirect(session_stripe.url, code=303)

@app.route('/success')
@login_required
def success():
    session.pop('cart', None)
    return render_template('success.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
