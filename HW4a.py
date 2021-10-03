import requests
import json
#from github import Github
#import pprint

token = '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'
ID = input("What is your Github username: ")
url = f"https://api.github.com/users/{ID}/repos"


response_repo = requests.get(url)
data_repo = response_repo.json()

for repository in data_repo:
    repo = repository["name"]
    print("Repo: ", repo)

    url_commit = f"https://api.github.com/repos/{ID}/{repo}/commits"
    response_commit = requests.get(url_commit)
    data_commit = response_commit.json()

    for commit in data_commit:
        c = enumerate(commit["sha"])
        print("Commit info: ", c)
    



"""
url_commit = f"https://api.github.com/repos/{ID}/{repo}/commits"

response_commit = requests.get(url_commit)

data_commit = response_commit.json()

n = len(data_commit)

print(data_commit)
print(n)
"""