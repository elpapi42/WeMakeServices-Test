from flask import redirect, url_for, jsonify, render_template
from flask_dance.contrib.github import github

from . import repos_bp

@repos_bp.route("/")
def render_profile():
    if(not github.authorized):
        return redirect(url_for("github.login"))
    
    # Retrieves username
    user_resp = github.get("/user").json()
    username = user_resp.get("login")
    avatar_url = user_resp.get("avatar_url")

    # Retrieves repos list
    repos_resp = github.get("/users/{}/repos".format(username)).json()

    repos_list = list()
    for repo in repos_resp:
        # Create a dict for append
        repo_dict = {
            "name": repo.get("name"),
            "url": repo.get("html_url"),
            "forks": repo.get("forks_count"),
        }

        repos_list.append(repo_dict)

    user_data = {
        "username": username, 
        "avatar_url": avatar_url, 
        "repos": repos_list
    }

    return render_template("user_data.html", user_data=user_data)
