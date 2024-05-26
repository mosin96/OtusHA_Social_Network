#!/usr/bin/env python

import connexion
import openapi_server.database # NOQA
from openapi_server import encoder
from openapi_server.database.init import init_users_table
from flask_jwt_extended import JWTManager


def main():
    init_users_table()
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config['JWT_SECRET_KEY'] = 'super-secret' # TODO перенести в переменные окружения
    jwt = JWTManager(app.app)
    app.add_api('openapi.yaml',
                arguments={'title': 'OTUS HA Social Network'},
                pythonic_params=True)
    app.run(port=8280)


if __name__ == '__main__':
    main()
