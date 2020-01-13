from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask

from application.repos import repos_bp

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

        return app


