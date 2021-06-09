import os
import secrets
from Flask_blog import app, bcrypt, db
from Flask_blog.form import LoginForm, RegistrationForm, PostForm,ProfileForm
from Flask_blog.models import User, Blog
from flask import flash,render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime 


@app.route('/')
def index():
	posts=Blog.query.all()
	return render_template('index.html',posts=posts)


@app.route('/login', methods=['POST','GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user,remember=form.remember_me.data)
			return redirect(url_for('index'))
	return render_template('login.html',form=form)


@app.route('/signup', methods=['POST','GET'])
def signup():
	if current_user.is_authenticated:
		return redirect('index')

	form = RegistrationForm()

	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user_1 = User(full_name=form.full_name.data, user_name=form.user_name.data,email=form.email.data,password=hashed_password)
		db.session.add(user_1)
		db.session.commit()
		return redirect(url_for("login"))
	return render_template('signup.html', form=form)


@app.route('/logout')
def log_out():
	print("logout is called")
	logout_user()
	return redirect(url_for('login'))


@app.route('/editprofile',methods=['POST','GET'])
@login_required
def editProfile():
	form = ProfileForm()
	if form.validate_on_submit():
		current_user.user_name = form.user_name.data
		current_user.full_name = form.full_name.data
		current_user.password = form.password.data
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('editProfile.html', form = form)

@app.route('/editpost',methods=['POST','GET'])
@login_required
def editPost():
	return "Blog editing post is complited"


@app.route('/addblog',methods=['POST','GET'])
@login_required
def addPost():
	form = PostForm()
	res = form.validate_on_submit()
	if res:
		user_1 = Blog(title=form.title.data, context = form.context.data,author=current_user.id)
		db.session.add(user_1)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('addPost.html', form=form)

