from app import app, db
from models import User
from flask import render_template, redirect, url_for
from form.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>der parol</h1>'
        #return '<h1>' + form.nickname.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(fullname=form.fullname.data,
                        nickname=form.nickname.data,
                        email=form.email.data,
                        password=hashed_password,
                        age=form.age.data)
                        
        db.session.add(new_user)
        db.session.commit()

        return '<h1>zapysav</h1>'
        #return '<h1>' + form.nickname.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/homeworks')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.fullname)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))