import os
import psycopg2
from psycopg2 import pool

os.environ['POSTGRES_DB'] = 'HA_SN_db'
os.environ['POSTGRES_USER'] = 'HA_SN_user'
os.environ['POSTGRES_PASSWORD'] = 'HA_SN_password'

# Uncomment for debug
# os.environ['POSTGRES_HOST'] = 'localhost'


def get_environment_variable(variable_name):
    """
    Get the value of an environment variable
    :param variable_name: The name of the environment variable
    :return: The value of the environment variable
    :raises: KeyError if the environment variable is not found
    """
    value = os.getenv(variable_name)
    if value is None:
        raise KeyError(f'Environment variable {variable_name} is not set')
    return value


DB_HOST = get_environment_variable('POSTGRES_HOST')
DB_NAME = get_environment_variable('POSTGRES_DB')
DB_USER = get_environment_variable('POSTGRES_USER')
DB_PASSWORD = get_environment_variable('POSTGRES_PASSWORD')

connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,  # Минимальное количество соединений в пуле
    2000,  # Максимальное количество соединений в пуле
    host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)


# Контекстный менеджер для работы с соединением
class ConnectionFromPool:
    def __enter__(self):
        self.conn = connection_pool.getconn()
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        connection_pool.putconn(self.conn)
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            # Можно обработать ошибку здесь, если необходимо

