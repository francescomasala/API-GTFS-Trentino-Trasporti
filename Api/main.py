from flask import Flask
from Api.Blueprints import attributions, docs, fares, realtime, routes, trips, stops
app = Flask(__name__)


@app.route('/')
def hello_world() :  # put application's code here
    return 'Hello World!'


if __name__ == '__main__' :
    app.register_blueprint(attributions.bp)
    app.register_blueprint(docs.bp)
    app.register_blueprint(routes.bp)
    app.register_blueprint(trips.bp)
    app.register_blueprint(fares.bp)
    app.register_blueprint(realtime.bp)
    app.register_blueprint(stops.bp)
    app.run()
