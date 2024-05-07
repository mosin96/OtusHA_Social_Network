#!/usr/bin/env python

import connexion
from openapi_server.database import connection
from openapi_server import encoder
from openapi_server.database.init import init_users_table


def main():
    init_users_table()
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'OTUS HA Social Network'},
                pythonic_params=True)
    app.run(port=8280)


if __name__ == '__main__':
    main()
