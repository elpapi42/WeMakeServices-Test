from . import repos_bp

@repos_bp.route("/")
def render_repos():
    return "repos"