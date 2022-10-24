from __main__ import app
from flask import make_response, request
from modules.beam import BeamRoute
from modules.walk import WalkRoute

@app.route('/beam', methods=['POST'])
def beam():
    data = request.get_json()
    if ("org" and "dst") in data:
        beam = BeamRoute(data["org"], data["dst"])
        return make_response(beam.createResponse(), 200)
    else:
        return make_response({"error" : "this api request 2 parameters ([org], [dst])"}, 200)

@app.route('/popbus', methods=['POST'])
def popbus():
    return make_response({"popbus" : "This feature is unavailable"}, 200)

@app.route('/walk', methods=['POST'])
def walk():
    data = request.get_json()
    if ("org" and "dst") in data:
        walk = WalkRoute(data["org"], data["dst"])
        return make_response(walk.createResponse(), 200)
    else:
        return make_response({"error" : "this api request 2 parameters ([org], [dst])"}, 200)