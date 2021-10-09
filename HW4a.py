import requests
import json
import unittest
#from github import Github
#import pprint

def github(x):
    rep = []
    final = []

    ID = x
    url = f"https://api.github.com/users/{ID}/repos"

    response_repo = requests.get(url)
    data_repo = response_repo.json()

    for repository in data_repo:
        rep.append(repository['name'])
    for c in rep:
        url_commit = f"https://api.github.com/repos/{ID}/{c}/commits"
        response_commit = requests.get(url_commit)
        data_commit = response_commit.json()
        
        commit = len(data_commit)        
        final.append('Repo: ' + c + ' Commit info: ' + str(commit))
    return final
        
if __name__ == '__main__':
    for item in github(input("What is your Github username: ")):
        print(item)

