
from flask import Flask, request, make_response, jsonify
from flask.json import jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import sys
from os.path import dirname,abspath
app = Flask(__name__)
cors = CORS(app)
api = Api(app)
version = "0.0"
# to support relative import 
sys.path.append(dirname(dirname(abspath(__file__))))
from Algorthims.postional_index_model import Positional_index
from Algorthims.vector_space_model import VectorSpace

phrase = Positional_index()
freetext = VectorSpace()

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
            return make_response(jsonify(phrase.phraseQueryWrapper(args['text'])), 200)
        if args['type']=="ftq":
            return make_response(jsonify(freetext.freeTextQueryWrapper(args['text'])), 200)
        return make_response(jsonify(), 200)

api.add_resource(ApiRoot, '/')
api.add_resource(ApiVer, '/query')

if __name__ == '__main__':
    app.run(debug=True)
