from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorlus.db'
app.config['SECRET_KEY'] = 'your-secret-key'

# E-maili serveri konfiguratsioon
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Muuda oma SMTP serveriks
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Muuda oma e-posti aadressiks
app.config['MAIL_PASSWORD'] = 'your-password'  # Muuda oma e-posti salasõnaks

db = SQLAlchemy(app)
mail = Mail(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Paroolid ei kattu. Palun proovi uuesti.")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        send_confirmation_email(email)

        flash("Registreerimine õnnestus! Palun kontrolli oma e-posti, et kinnitada konto.")
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            flash("Sisselogimine õnnestus!")
            return redirect(url_for('home'))
        else:
            flash("Vale e-posti aadress või parool.")
            return redirect(url_for('login'))
    return render_template('login.html')


def send_confirmation_email(email):
    msg = Message('Konto kinnitamine - E-mentorx',
                  sender='your-email@example.com',
                  recipients=[email])
    msg.body = "Tere! Palun kliki järgneval lingil, et kinnitada oma konto: http://127.0.0.1:5000/confirm"
    mail.send(msg)


@app.route('/confirm')
def confirm():
    flash("Konto on edukalt kinnitatud!")
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()  # Loob andmebaasi tabelid, kui neid pole
    app.run(debug=True)
