from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:21122004@localhost/flask'
db = SQLAlchemy(app)

class Vis(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='ownned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1030), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('vis.id'))

with app.app_context():
    db.create_all()  # Ensure tables are created
    existing_user = Vis.query.filter_by(username='Jordan').first()
    if not existing_user:
        print("User does not exist, adding user...")
        user = Vis(username='Jordan', email_address='jordan@email.com', password_hash='securepassword')
        db.session.add(user)
        db.session.commit()
        print("User added successfully.")
    else:
        print("User with this username already exists.")

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market():
    items = Vis.query.all()
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
