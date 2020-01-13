from flask import Blueprint

repos_bp = Blueprint("repos_bp", __name__)

from . import routes