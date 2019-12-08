
from flask import Flask, request, make_response, jsonify
from flask.json import jsonify
from flask_restful import Resource, Api, reqparse
import sys
from os.path import dirname,abspath
app = Flask(__name__)
api = Api(app)
version = "0.0"
# to support relative import 
sys.path.append(dirname(dirname(abspath(__file__))))
from Algorthims.postional_index_model import Positional_index
# from Algorthims.vector_space_model import Positional_index

phrase = Positional_index()

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
        print(args)
        if args['type']=="phrase":
            return make_response(jsonify(args,phrase.phraseQuery(args['text'])), 200)
        return make_response(jsonify(), 200)

api.add_resource(ApiRoot, '/')
api.add_resource(ApiVer, '/query')

if __name__ == '__main__':
    app.run(debug=True)
