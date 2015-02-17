from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, PackageLoader
from forms import UserSubmit
from github_viz import githubViz
import urllib2
import urllib
import json
import re

app = Flask(__name__)

id = #client id
secret = #client secret

@app.route('/', methods=['GET', 'POST'])
def index(follower=None):
	
	if request.method =='GET' and 'username' in request.args:
		form = UserSubmit()
		username = request.args['username']

		git_data = githubViz(username, id, secret)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, username = username)

	elif request.method =='GET':
		return redirect('/git_auth')

	elif request.method == 'POST':
		form = UserSubmit()

		username = request.form.get('username')
		git_data = githubViz(username, id, secret)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, username = username)	

@app.route('/?username=<follower>', methods=['GET', 'POST'])
def follower(follower=None):
	form = UserSubmit()

	if request.method == 'GET':
		username = follower
		git_data = githubViz(username)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, username = follower)

@app.route('/user_chart', methods=['GET', 'POST'])
def callback():
	form = UserSubmit()

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

		get_url = urllib2.urlopen('https://api.github.com/user?access_token=' + token)
		get_string = json.load(get_url)
		username = get_string['login']

		return redirect(url_for('.index', username=username))
	except (ValueError, KeyError, TypeError):
		return render_template('github_viz.html', form=form)	

@app.route('/git_auth', methods=['GET', 'POST'])
def git():
	
	return render_template('git_auth.html', id=id, secret=secret)

if __name__ == '__main__':
	app.run(debug=True)