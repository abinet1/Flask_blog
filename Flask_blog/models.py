from Flask_blog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(50), nullable=False, unique=False)
	user_name = db.Column(db.String(30), nullable=False, unique=True)
	email = db.Column(db.String(125), nullable=False, unique=True)
	profile_pic = db.Column(db.String(20), nullable=True, unique=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False, unique=False)
	blog = db.relationship('Blog', backref='writer', lazy=True)

	def __repr__(self):
		return f"User('{self.id}','{self.user_name}','{self.full_name}','{self.email}')"

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(30), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	recently_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	context = db.Column(db.Text, nullable=False)
	author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Blog('{self.id}','{self.title}','{self.date}','{self.author}')"