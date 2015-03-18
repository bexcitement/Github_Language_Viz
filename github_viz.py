import requests

def githubViz(user, cl_id, cl_secret):
	r = requests.get('https://api.github.com/users/' + user + '/repos?per_page=1000&client_id=' + cl_id + '&client_secret=' + cl_secret)
	followers = requests.get('https://api.github.com/users/' + user + '/following?per_page=1000&client_id=' + cl_id + '&client_secret=' + cl_secret)
	
	json_response = r.json()
	json_followers = followers.json()
	followers = []
	dates = []  

	if isinstance(json_response, dict):
		languages_dict = 'sad face'
	else:
		languages_dict = {}
		for repo in json_response:
			if repo['language'] is None:
				continue
			else:
				if repo['language'] in languages_dict:
					languages_dict[repo['language']] += repo['size']
				else:
					languages_dict[repo['language']] = repo['size']
				dates.append(repo['pushed_at'])

		for follower in json_followers:
			followers.append(follower['login'])

	return languages_dict, followers, dates
