

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorlus.db'
app.config['SECRET_KEY'] = 'see-on-salajane-voti'

db = SQLAlchemy(app)

# Kasutaja mudel
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Küsimuste mudel
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

# Vastuste mudel
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship('Question')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

# Andmebaasi loomine
db.create_all()

# Avaleht
@app.route('/')
def home():
    questions = Question.query.all()
    return render_template('home.html', questions=questions)

# Sisselogimine
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        return 'Login Failed'
    return render_template('login.html')

# Küsimuse lisamine
@app.route('/add_question', methods=['POST'])
def add_question():
    if 'user_id' in session:
        content = request.form['content']
        question = Question(content=content, user_id=session['user_id'])
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('login'))

# Vastuse lisamine
@app.route('/add_answer/<int:question_id>', methods=['POST'])
def add_answer(question_id):
    if 'user_id' in session:
        content = request.form['content']
        answer = Answer(content=content, question_id=question_id, user_id=session['user_id'])
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


