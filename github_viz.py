import requests

def githubViz(user):
	r = requests.get('https://api.github.com/users/' + user + '/repos?per_page=1000')
	followers = requests.get('https://api.github.com/users/' + user + '/followers?per_page=1000')
	
	json_response = r.json()
	json_followers = followers.json()
	# print json_response
	# print json_followers

	if isinstance(json_response, dict):
		languages_dict = 'sad face'
	else:
		languages_dict = {}
		followers = []
		for repo in json_response:
			for key, value in repo.iteritems():	
				if repo['language'] == None:
					continue
				else: 
					if repo['language'] in languages_dict:
						languages_dict[repo['language']] += repo['size']
					else:
						languages_dict[repo['language']] = repo['size']

		for follower in json_followers:
			followers.append(follower['login'])

	return languages_dict, followers
