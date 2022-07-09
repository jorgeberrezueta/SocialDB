from flask import Flask
# from flask_restful import Api
from middleware.authenticate import authenticate

import routes

class Server:

    def __init__(self):
        self.app = Flask(__name__)

        # Register middleware
        self.app.wsgi_app = authenticate(self.app.wsgi_app)

        # Register routes
        routes.register(self.app)


    def start(self, debug=False):
        self.app.run(debug=True)
