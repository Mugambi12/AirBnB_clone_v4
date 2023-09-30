#!/usr/bin/python3

'''
Flask with general routes

Routes:
    - /status: Display {"status": "OK"}
    - /stats: Display total for all classes
'''

from flask import jsonify
from models import storage
from api.v1.views import app_views

# Task 3
@app_views.route("/status", methods=['GET'])
def status():
    '''
    Return JSON of OK status
    '''
    return jsonify({'status': 'OK'})

# Task 4
@app_views.route("/stats", methods=['GET'])
def storage_counts():
    '''
    Return counts of all classes in storage
    '''
    cls_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(cls_counts)
