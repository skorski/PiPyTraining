from datetime import datetime
import mysqldb
import peewee as pw
from peewee import *
 
pwdb = pw.MySQLDatabase("sql353995", host="sql3.freemysqlhosting.net", port=3306, user="sql353995", passwd="cQ1%fU8%")

class MySQLModel(pw.Model):
	UID = PrimaryKeyField(unique=True, null=False)
	class Meta:
		database = pwdb

class Requests(MySQLModel):
	PIN = IntegerField()
	Value = TextField()
	TS = DateTimeField()

pwdb.connect

from flask import (
	Flask,
	abort,
	flash,
	redirect,
	render_template,
	request,
	url_for
	)

from flask.ext.stormpath import (
	StormpathError,
	StormpathManager,
	User,
	login_required,
	login_user,
	user
	)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '6fZIfY+2kEcQFd69t2GHPJEqlGCQcLPIe96ehFtXlQw'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'flaskr'

stormpath_manager = StormpathManager(app)

# @app.before_request
# def before_request():
# 	pwdb.connect()

# @app.after_request
# def after_request(response):
# 	pwdb.close()
# 	return response

@app.route('/')
def show_posts():
	posts = []
	for account in stormpath_manager.application.accounts:
		if account.custom_data.get('posts'):
			posts.extend(account.custom_data['posts'])

	posts = sorted(posts, key=lambda k: k['date'], reverse = True)
	return render_template('show_posts.html', posts=posts)

@app.route('/dbread')
def query_db():
	posts = []
	for account in stormpath_manager.application.accounts:
		if account.custom_data.get('posts'):
			posts.extend(account.custom_data['posts'])

	posts = sorted(posts, key=lambda k: k['date'], reverse = True)
	return render_template('show_posts.html', posts=posts)

@app.route('/dbwrite')
def write_db():
	pwdb.connect()
	try:
		with pwdb.transaction():
			RQ = Requests.create(
				PIN = 18,
				Value = "On",
				TS = datetime.datetime.now()
				)
			return redirect(url_for('show_posts'))
	except Exception, e:
		flash('There was an error adding that request')

	pwdb.close()
	return redirect(url_for('show_posts'))


@app.route('/add', methods=['POST'])
@login_required
def add_post():
	if not user.custom_data.get('posts'):
		user.custom_data['posts'] = []

	user.custom_data['posts'].append({
		'date': datetime.utcnow().isoformat(),
		'title': request.form['title'],
		'text': request.form['text']
		})

	user.save()

	flash('New post successfully added.')

	return redirect(url_for('show_posts'))

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	try:
		_user = User.from_login(
			request.form['email'],
			request.form['password']
			)

		login_user(_user, remember = True)
		flash('You were logged in.')

		return redirect(url_for('show_posts'))

	except StormpathError, err:
		error = err.message

	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	logout_user()
	flash('You were logged out.')

	return redirect(url_for('show_posts'))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)

