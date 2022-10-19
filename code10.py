import requests
from pprint import pprint
username="Vani-Adimulam"
url=f"https://api.github.com/users/{username}"
user_data=requests.get(url).json()
print(user_data)
import base64
from github import Github
username="Vani-Adimulam"
g=Github()
user=g.get_user(username)
for repo in user.get_repos():
   print(repo)