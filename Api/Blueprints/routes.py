from flask import Blueprint, render_template

bp = Blueprint("routes", __name__, url_prefix="/routes")


@bp.route("/")
def api_index() :
    return render_template('api/api.html', title="API - ")
