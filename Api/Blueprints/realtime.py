from flask import Blueprint, render_template

bp = Blueprint("realtime", __name__, url_prefix="/realtime")


@bp.route("/")
def api_index() :
    return render_template('api/api.html', title="API - ")
