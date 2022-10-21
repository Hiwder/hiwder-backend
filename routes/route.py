from __main__ import app
from flask import make_response

@app.route('/beam', methods=['POST'])
def beam():
    return make_response({"test" : "Success"}, 200)

@app.route('/popbus', methods=['POST'])
def popbus():
    return make_response({"popbus" : "This feature is unavailable"}, 200)

@app.route('/walk', methods=['POST'])
def walk():
    return make_response({"walk" : "This feature is unavailable"}, 200)