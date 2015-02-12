from flask import Flask, render_template, request
from jinja2 import Environment, PackageLoader
from forms import UserSubmit
from github_viz import githubViz

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(follower=None):

	form = UserSubmit()

	if request.method =='GET':
		return render_template('github_viz.html', form=form)

	elif request.method == 'POST':
		username = request.form.get('username')
		git_data = githubViz(username)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
		return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, username = username)	

@app.route('/follower_chart/<follower>', methods=['GET', 'POST'])
def follower(follower=None):
	form = UserSubmit()

	if request.method == 'GET':
		username = follower
		git_data = githubViz(username)
		github_user = git_data[0]
		github_user_followers = sorted([x.encode('utf-8') for x in git_data[1]], key=lambda s: s.lower())
	return render_template('github_viz.html', form=form, github_viz = github_user, 
			followers = github_user_followers, username = follower)

if __name__ == '__main__':
	app.run(debug=True)