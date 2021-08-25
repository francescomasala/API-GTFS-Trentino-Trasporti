from flask import Blueprint, render_template

bp = Blueprint("fares", __name__, url_prefix="/fares")


@bp.route("/")
def api_index() :
    return render_template('api/api.html', title="API - ")
