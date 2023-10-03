#!/usr/bin/python3

'''
App for registering blueprint and starting Flask
'''

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

#Task 12
# Enable CORS and allow requests from any origin:
CORS(app, resources={r' /api/v1/*': {'origin': '0.0.0.0'}})

# Register the app_views blueprint:
app.register_blueprint(app_views)
app.url_map.strict_slashes = False

# Teardown function to close the SQLAlchemy Session object after each request:
@app.teardown_appcontext
def tear_down(exception):
    '''
    Close query after each session
    '''
    storage.close()

# Task 5
#Error handler for 404 Not Found:
@app.errorhandler(404)
def not_found(error):
    '''
    Return JSON formatted 404 status code response
    '''
    response = {'error': 'Not found'}
    return jsonify(response), 404

"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(
        host=getenv("HBNB_API_HOST", "0.0.0.0"),
        port=int(getenv("HBNB_API_PORT", "5000")),
        threaded=True
    )
"""
