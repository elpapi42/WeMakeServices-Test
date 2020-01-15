# This Python file uses the following encoding: utf-8

"""Defines the routes that will be attached to the blueprint."""

from flask import redirect, url_for, render_template
from flask_dance.contrib.github import github


def render_profile():
    """
    Gather and render data from github account of the authenticated user.

    Returns:
        html template with user data

    """
    if (not github.authorized):
        return redirect(url_for('github.login'))

    # Retrieves username
    user_resp = github.get('/user').json()
    username = user_resp.get('login')
    avatar_url = user_resp.get('avatar_url')

    repos_list = get_repos(username)

    user_data = {
        'username': username,
        'avatar_url': avatar_url,
        'repos': repos_list,
    }

    return render_template('user_data.html', user_data=user_data)


def get_repos(username):
    """
    Retieves the github repos associated with the username provided.

    Args:
        username (str): github username

    Returns:
        A list of repos, each item with repo data

    """
    # Retrieves repos list
    repos_resp = github.get(
        '/users/{username}/repos'.format(username=username),
    ).json()

    # Extract the required data from each repo
    repos_list = []
    for repo in repos_resp:
        # Create a dict for append
        repo_dict = {
            'name': repo.get('name'),
            'url': repo.get('html_url'),
            'forks': repo.get('forks_count'),
        }

        repos_list.append(repo_dict)

    return repos_list
