from openapi_server.database import connection


def init_users_table():
    # Инициализируем таблицу
    conn = connection.get_db_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
        cur.execute('CREATE TABLE IF NOT EXISTS cdm.users'
                    '(id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,'
                    'first_name VARCHAR(50) NOT NULL,'
                    'second_name VARCHAR(50) NOT NULL,'
                    'birthdate DATE NOT NULL,'
                    'biography TEXT,'
                    'city VARCHAR(50),'
                    'password_hash BYTEA NOT NULL)')
        conn.commit()
        conn.close()
