import bcrypt
import connexion
import six
import time
import random

from openapi_server.database import connection
from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response500 import InlineResponse500  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import create_access_token


def login_post(inline_object=None):  # noqa: E501
    """login_post

    Упрощенный процесс аутентификации путем передачи идентификатор пользователя и получения токена для дальнейшего прохождения авторизации # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse200
    """
    def authenticate_user(auth_request: InlineObject):
        conn = connection.get_db_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT password_hash FROM cdm.users "
                    f"WHERE id=\'{auth_request.id}\'")
        result = cur.fetchone()
        if result:
            stored_hash = result[0]
            stored_hash_bytes = bytes(stored_hash)
            if bcrypt.checkpw(auth_request.password.encode('utf-8'), stored_hash_bytes):
                return True
        return False
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
        if authenticate_user(inline_object):
            return InlineResponse200(token=create_access_token(identity=inline_object.id))
        return 'Not do some magic!'# TODO ошибки если пароль не правильный и пользователь не найден и 500 на остальное




def user_get_id_get(id):  # noqa: E501
    """user_get_id_get

    Получение анкеты пользователя # noqa: E501

    :param id: Идентификатор пользователя
    :type id: str

    :rtype: User
    """

    return 'do some magic!'


def user_register_post(inline_object1=None):  # noqa: E501
    """user_register_post

    Регистрация нового пользователя # noqa: E501

    :param inline_object1: 
    :type inline_object1: dict | bytes

    :rtype: InlineResponse2001
    """
    request_id = str(time.time_ns()) + str(random.randint(1, 1000))
    try:
        if connexion.request.is_json:
            inline_object1 = InlineObject1.from_dict(connexion.request.get_json())
            # Хеширование пароля
            password_hash = bcrypt.hashpw(inline_object1.password.encode('utf-8'), bcrypt.gensalt())
            # Выполнение SQL запроса для вставки нового пользователя в таблицу
            conn = connection.get_db_connection()
            if conn is not None:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO cdm.users (first_name, second_name, birthdate, biography, city, password_hash)"
                    "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                    (inline_object1.first_name, inline_object1.second_name, inline_object1.birthdate,
                     inline_object1.biography, inline_object1.city, password_hash)
                )
                user_id = cur.fetchone()[0]
                conn.commit()
                response = InlineResponse2001(user_id)
                return response
    except Exception:
        response = InlineResponse500(message='Ошибка создания пользователя', code=500, request_id=request_id)
        return connexion.problem(response.code, response.message, response.to_str()) #TODO подумать над ответом

