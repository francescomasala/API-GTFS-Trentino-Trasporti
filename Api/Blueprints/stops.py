from flask import Blueprint, render_template, request

bp = Blueprint("stops", __name__, url_prefix="/stops")


@bp.route("/")
def stops_index():

    return render_template('api/api.html', title="API - ")


@bp.route("/byStopID")
def stops_id():
    stopId = request.args.get('stopId')
    return render_template('api/api.html', title="API - ")


@bp.route("/byLatLon")
def stops_lat_lon():
    stopLat = request.args.get('stopLat')
    stopLon = request.args.get('stopLon')
    stopDistance = request.args.get('stopDistance')
    return render_template('api/api.html', title="API - ")


@bp.route("/byStopName")
def stops_name():
    stopName = request.args.get('stopName')
    return ('The args are: ' + stopName)
