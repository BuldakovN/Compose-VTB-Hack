import flask
from flask import jsonify
import flask_restful
from api_db import *



app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = flask_restful.Api()



class HelloWorld(flask_restful.Resource):
    def get(self, user_type, date):
        if date == 0:
            return main_news(user_type)
        else:
            return ['hello', '123', 'пвп']


api.add_resource(HelloWorld, '/api/main/<string:user_type>/<int:date>')
api.init_app(app)


# для запуска api
if __name__ == "__main__":
    app.run(debug=True, port=1707, host="0.0.0.0")
