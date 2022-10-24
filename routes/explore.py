from app import app, db
from flask import make_response, request

@app.route('/explore', methods=['POST'])
def explore():

    data = request.get_json()

    if ("tag") in data:

        tag = data["tag"]

        query = db.collection('items').where('tags', 'array_contains', tag).get()

        items = [item.to_dict() for item in query]

        return make_response({"items" : items}, 200)

    else:
        return make_response({"error" : "this api request 1 parameters (tag)"}, 200)

    