# This Python file uses the following encoding: utf-8

"""Production application config."""

import os

DEBUG = False
TESTING = False

GITHUB_OAUTH_CLIENT_ID = os.environ.get('GITHUB_OAUTH_CLIENT_ID')
GITHUB_OAUTH_CLIENT_SECRET = os.environ.get('GITHUB_OAUTH_CLIENT_SECRET')

SECRET_KEY = os.environ.get('SECRET_KEY')
