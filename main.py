from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class StarSystems(Resource):
    def get(self):
        f = open('StarSystems.json')
        data = json.load(f)
        f.close()
        return data, 200

api.add_resource(StarSystems, '/starSystems')

if __name__ == '__main__':
    app.run()
