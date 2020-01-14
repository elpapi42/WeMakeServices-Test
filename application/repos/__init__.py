from flask import Blueprint

repos_bp = Blueprint("repos_bp", __name__, template_folder='templates')

from . import routes