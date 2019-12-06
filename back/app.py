
from flask import Flask, request, make_response, jsonify
from flask.json import jsonify
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)
version = "0.0"

class ApiRoot(Resource):
    def get(self):
        root_data = {
            "name": "IR-System",
            "version": version,
        }
        return make_response(jsonify(root_data), 200)


class ApiVer(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type')
        parser.add_argument('text')
        args = parser.parse_args()
        return make_response(jsonify(version), 200)

api.add_resource(ApiRoot, '/')
api.add_resource(ApiVer, '/query')

if __name__ == '__main__':
    app.run(debug=True)
