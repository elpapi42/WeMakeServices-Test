# This Python file uses the following encoding: utf-8

"""Gather data from github user and render an html templatewith that data."""

from flask import Blueprint

from application.repos.routes import render_profile

repos_bp = Blueprint('repos_bp', __name__, template_folder='templates')

repos_bp.add_url_rule('/', view_func=render_profile)
