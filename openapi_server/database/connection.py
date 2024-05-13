import os
import psycopg2

os.environ['POSTGRES_DB'] = 'HA_SN_db'
os.environ['POSTGRES_USER'] = 'HA_SN_user'
os.environ['POSTGRES_PASSWORD'] = 'HA_SN_password'


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


# Функция для подключения к базе данных PostgreSQL
def get_db_connection():
    try:
        DB_HOST = get_environment_variable('POSTGRES_HOST')
        DB_NAME = get_environment_variable('POSTGRES_DB')
        DB_USER = get_environment_variable('POSTGRES_USER')
        DB_PASSWORD = get_environment_variable('POSTGRES_PASSWORD')

        connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        return connection
    except psycopg2.Error as e:
        print(f'Ошибка при подключении к базе данных: {e}')
        return None
    except KeyError as e:
        print(f'Ошибка: {e}')
        return None
