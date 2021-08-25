from flask import Blueprint, render_template

bp = Blueprint("docs", __name__, url_prefix="/docs")


@bp.route("/")
def api_index() :
    return render_template('api/api.html', title="API - ")
