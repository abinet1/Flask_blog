from Flask_blog import app, bcrypt, db
from Flask_blog.form import LoginForm, RegistrationForm
from Flask_blog.models import User, Blog
from flask import flash,render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user

@app.route('/')
def index():
	posts=Blog.query.all()
	print(posts)
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
			print(f'welcome {{user.full_name.data}}','success')
			return redirect(url_for('index'))
	return render_template('login.html',form=form)

@app.route('/signup', methods=['POST','GET'])
def signup():
	if current_user.is_authenticated:
		return redirect('index')

	form = RegistrationForm()

	if form.validate_on_submit():
		print("here 1")
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		print("here 2")
		user_1 = User(full_name=form.full_name.data, user_name=form.user_name.data,email=form.email.data,password=hashed_password)
		print("here 3")
		db.session.add(user_1)
		print("here 4")
		db.session.commit()
		print(f'welcome','success')
		return redirect(url_for("login"))
	return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/editprofile',methods=['POST','GET'])
def editProfile():
	return "Blog editing profile is done"

@app.route('/editpost',methods=['POST','GET'])
def editPost():
	return "Blog editing post is complited"

@app.route('/addblog',methods=['POST','GET'])
def addPost():
	return "Blog adding is complited successfuly"

