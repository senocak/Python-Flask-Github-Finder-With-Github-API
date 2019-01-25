from flask import Flask, render_template, request, json
import requests
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    users = requests.get("https://api.github.com/users/senocak") 
    if "message" in users.json():
        pass
    else:
        with open('users.json', 'w') as outfile:
            json.dump(users.json(), outfile)

    followers = requests.get("https://api.github.com/users/senocak/followers") 
    if "message" in followers.json():
        pass
    else:
        with open('followers.json', 'w') as outfile:
            json.dump(followers.json(), outfile)

    followings = requests.get("https://api.github.com/users/senocak/following") 
    if "message" in followings.json():
        pass
    else:
        with open('followings.json', 'w') as outfile:
            json.dump(followings.json(), outfile)

    repos = requests.get("https://api.github.com/users/senocak/repos") 
    if "message" in repos.json():
        pass
    else:
        with open('repos.json', 'w') as outfile:
            json.dump(repos.json(), outfile)

    users_from_file = ""
    with open('users.json') as json_file:  
        data = json.load(json_file)
        users_from_file=data

    followers_from_file = ""
    with open('followers.json') as json_file:  
        data = json.load(json_file)
        followers_from_file=data

    followings_from_file = ""
    with open('followings.json') as json_file:  
        data = json.load(json_file)
        followings_from_file=data
    
    repos_from_file = ""
    with open('repos.json') as json_file:  
        data = json.load(json_file)
        repos_from_file=data

    return render_template("index.html",profile = users_from_file , followers = followers_from_file, followings=followings_from_file, repos=repos_from_file)

if __name__ == "__main__":
    app.run(debug=True)