from app import app, db
from flask import make_response, request
import geopy.distance

@app.route('/items-list', methods=['GET', 'POST'])
def items_list():

    items = [item.to_dict() for item in db.collection('items').stream()]

    if request.method == 'GET':
        return make_response({"items" : items}, 200)

    if request.method == 'POST':

        data = request.get_json()

        if ("location") in data:

            for item in items:
                dst = tuple(item["location"])
                org = tuple(data["location"])
                
                distance = geopy.distance.geodesic(org, dst).km
                item["distance"] = float("{0:.1f}".format(distance))

            return make_response({"items" : items}, 200)


        else:
            return make_response({"error" : "this api request 2 parameters ([org], [dst])"}, 200)