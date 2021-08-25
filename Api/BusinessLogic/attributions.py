from flask import Blueprint, render_template

bp = Blueprint("attributions", __name__, url_prefix="/attributions")


@bp.route("/")
def api_index() :
    return render_template('api/api.html', title="API - ")
