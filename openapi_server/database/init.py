from openapi_server.database.connection import ConnectionFromPool


def init_users_table():
    # Инициализируем таблицу
    with ConnectionFromPool() as connection:
        with connection.cursor() as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
            cur.execute('CREATE SCHEMA IF NOT EXISTS cdm')
            cur.execute('CREATE TABLE IF NOT EXISTS cdm.users'
                        '(id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,'
                        'first_name VARCHAR(50) NOT NULL,'
                        'second_name VARCHAR(50) NOT NULL,'
                        'birthdate DATE NOT NULL,'
                        'biography TEXT,'
                        'city VARCHAR(50),'
                        'password_hash BYTEA NOT NULL)')
            connection.commit()
        with connection.cursor() as cur2:
            cur2.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
            cur2.execute('CREATE INDEX IF NOT EXISTS idx_gin_users_name ON cdm.users '
                         'USING gin (first_name gin_trgm_ops, second_name gin_trgm_ops);')
            connection.commit()
