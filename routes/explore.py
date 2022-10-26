from app import app, db
from flask import make_response, request
import geopy.distance

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

@app.route('/near-you', methods=['POST'])
def near_you():

    near_items = list()

    items = [item.to_dict() for item in db.collection('items').stream()]

    data = request.get_json()

    if ("location" and "radius") in data:

        for item in items:
            dst = tuple(item["location"])
            org = tuple(data["location"])
            radius = float(data["radius"])

            distance = geopy.distance.geodesic(org, dst).km

            if distance <= radius:
                item["distance"] = float("{0:.1f}".format(distance))
                near_items.append(item)

        return make_response({"items" : near_items}, 200)

    else:
        return make_response({"error" : "this api request 2 parameters ([location], radius)"}, 200)
