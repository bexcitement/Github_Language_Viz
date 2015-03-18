from flask import Flask, render_template, request, redirect, url_for, session
from jinja2 import Environment, PackageLoader
from forms import UserSubmit
from github_viz import githubViz
from flask_oauth import OAuth
import urllib2
import urllib
import json
import re

app = Flask(__name__)
oauth = OAuth()

id = #client_id
secret = #client_secret

@app.route('/', methods=['GET', 'POST'])
def index(follower=None):

	if request.method =='GET' and 'github_token' not in session:
		return redirect('/githubviz/landing_page')

	elif request.method =='GET' and session['github_token'] and 'username' in request.args:
		print 'Other user'
		form = UserSubmit()
		username = request.args['username']
		code = session['github_token']

		git_data = githubViz(username, id, secret)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		# if no date returned from repos, set to launch date of github
		github_date = sorted([x.encode('utf-8') for x in git_data[2]])[0] if bool(git_data[2]) else '2008, 4, 10'

		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, dates = github_date, username = username, code = code, id=id, secret=secret)

	elif request.method =='GET' and session['github_token']:
		form = UserSubmit()
		username = session['github_user']
		code = session['github_token']

		git_data = githubViz(username, id, secret)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		# if no date returned from repos, set to launch date of github
		github_date = sorted([x.encode('utf-8') for x in git_data[2]])[0] if bool(git_data[2]) else '2008, 4, 10'

		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, dates = github_date, username = username, code = code, id=id, secret=secret)

	elif request.method == 'POST' and session['github_token']:
		form = UserSubmit()

		username = request.form.get('username')
		code = session['github_token']
		git_data = githubViz(username, id, secret)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		github_date = sorted([x.encode('utf-8') for x in git_data[2]])[0] if bool(git_data[2]) else '2008, 4, 10'
		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, dates = github_date, username = username, code=code, id=id, secret=secret)	

@app.route('/user_chart', methods=['GET', 'POST'])
def callback():
	form = UserSubmit()
	print 'here too'

	try:
		session_code = request.args.get('code')
		url = 'https://github.com/login/oauth/access_token'
		values = {'client_id' : id,
	          'client_secret' : secret,
	          'code' : session_code,
	          'Content-Type': 'application/json' }

		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		string = response.read()
		token = re.split('=([^;]*)&s', string)[1]
		session['github_token'] = session_code

		get_url = urllib2.urlopen('https://api.github.com/user?access_token=' + token)
		get_string = json.load(get_url)
		session['github_user'] = get_string['login']
		username = get_string['login']

		return redirect(url_for('.index', username=username))
	except (ValueError, KeyError, TypeError):
		return render_template('github_viz.html', form=form)	

@app.route('/landing_page', methods=['GET', 'POST'])
def landing_page():
	return render_template('git_auth.html', id=id, secret=secret)

if __name__ == '__main__':
	app.secret_key = secret
	app.run()
