from flask import Blueprint, render_template

bp = Blueprint("trips", __name__, url_prefix="/trips")


@bp.route("/")
def api_index() :
    return render_template('api/api.html', title="API - ")
