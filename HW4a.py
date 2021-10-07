import requests
import json
import unittest
#from github import Github
#import pprint
def github():
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
        
        commit_count = len(data_commit)        
        print("Commit info: ", commit_count)
        
#        for commit["sha"] in c:
#               n = len(c)
github()

class testingCommit(unittest.TestCase):
    def testInput(self):
        self.assertEqual(github())

