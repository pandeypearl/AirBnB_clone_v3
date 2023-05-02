#!/usr/bin/python3
""" States Views """
from flask import jsonify, make_response, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<id>/cities',
                 strict_slashes=False,
                 methods=['GET', 'POST'])
def view_cities_of_state(id):
    """ Returns list of all list objects """
    state = storage.get(State.id)

    if state is None:
        return abort(404)

    if request.method == 'GET':
        list = []
        for city in state.cities:
            list.append(city.to_dict())
        return jsonify(list)

    if request.method == 'POST':

        data = request.get_json()

        if isinstance(data, dict):
            pass
        else:
            return jsonify({"error": "Not a JSON"}), 400

        if 'name' not in data.keys():
            return jsonify({"error": "Missing name"}), 400

        if 'id' in data.keys():
            data.pop("id")
        if 'created_at' in data.keys():
            data.pop("created_at")
        if 'updated_at' in data.keys():
            data.pop("updated_at")

        data.update({"state_id": id})

        # Create object
        obj = City(**data)

        # Save object in storage
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<id>',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def view_city_id(id):
    """ Returns list of all objects, or delete object with given id """
    city = storage.get(City, id)

    if city is None:
        return abort(404)

    if request.method == 'GET':
        return jsonify(city.to_dict())

    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()
        if isinstance(data, dict):
            pass
        else:
            return jsonify({"error": "Not a JSON"}), 400

        if 'id' in data.keys():
            data.pop("id")
        if 'created_at' in data.keys():
            data.pop("created_at")
        if 'updated_at' in data.keys():
            data.pop("updated_at")

        for key, value in data.items():
            setattr(city, key, value)

        storage.save()
        return jsonify(city.to_dict())
