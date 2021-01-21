from flask import Flask
from flask_restful import Api

from routes import ProcessPayment

app = Flask(__name__)
api = Api(app=app)


api.add_resource(ProcessPayment, '/')

if __name__ == "__main__":
    app.run(debug=True)