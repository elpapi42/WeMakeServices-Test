from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask
from flask_dance.contrib.github import make_github_blueprint

from application.repos import repos_bp

github_bp = make_github_blueprint(
    scope="public_repo", 
    redirect_url="/repos/",
    login_url="/github/",
    authorized_url="/github/authorized/"
)

def create_app(testing=False):
    """ 
    Init core application 

    args:
        testing (bool): if true, the app will be ready for be tested using the test suit, default: False
    
    """
    # Load .env vars
    dotenv_path = join(dirname(dirname(__file__)), '.env')
    load_dotenv(dotenv_path)
    
    app = Flask("application", instance_relative_config=True)
    app.config.from_object("config")

    if(app.env == "development"):
        app.config.from_pyfile("development.py")
    
    if(testing):
        app.debug = True
        app.testing = True

    with app.app_context():
        app.register_blueprint(repos_bp, url_prefix="/repos")
        app.register_blueprint(github_bp, url_prefix="/")

        return app


