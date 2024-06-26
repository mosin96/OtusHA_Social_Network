import random
import time
from datetime import timedelta

import bcrypt
import connexion
from flask import request
from flask_jwt_extended import create_access_token, jwt_required

from openapi_server.database.connection import ConnectionFromPool
from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response500 import InlineResponse500  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.util import is_valid_uuid, get_user_info_from_database_search, jwt_user_in_database_required, \
    get_user_info_from_database_by_id


def login_post(inline_object=None):  # noqa: E501
    """login_post

    Упрощенный процесс аутентификации путем передачи идентификатор пользователя и получения токена для дальнейшего прохождения авторизации # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse200
    """

    def authenticate_user(auth_request: InlineObject):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT password_hash FROM cdm.users "
                               f"WHERE id=\'{auth_request.id}\'")
                select_result = cursor.fetchone()
        if select_result:
            stored_hash = select_result[0]
            stored_hash_bytes = bytes(stored_hash)
            if bcrypt.checkpw(auth_request.password.encode('utf-8'), stored_hash_bytes):
                return True
            return False
        return None

    request_id = str(time.time_ns()) + str(random.randint(1, 1000))
    try:
        if connexion.request.is_json:
            inline_object = InlineObject.from_dict(connexion.request.get_json())
            if not is_valid_uuid(inline_object.id):
                return "Невалидные данные", 400
            result = authenticate_user(inline_object)
            if result is None:
                return "Пользователь не найден", 404
            if result:
                new_token = create_access_token(identity=inline_object.id,
                                                expires_delta=timedelta(minutes=600),
                                                fresh=True
                                                )
                return InlineResponse200(token=new_token), 200
            return "Неправильный пароль", 403
        return "Невалидные данные", 400
    except Exception:
        response = InlineResponse500(message='Ошибка сервера', code=500, request_id=request_id)
        return response, response.code


@jwt_required(fresh=True)
@jwt_user_in_database_required
def user_get_id_get(id_, *args, **kwargs):
    """user_get_id_get

    Получение анкеты пользователя

    :param id_: Идентификатор пользователя
    :type id_: str

    :param id_: Идентификатор пользователя
    :type id_: str

    :rtype: User
    """
    if not is_valid_uuid(id_):
        return "Невалидные данные", 400
    user_info = get_user_info_from_database_by_id(id_)
    if user_info is None:
        return "Анкета не найдена", 404
    result_user = User(**user_info)
    return result_user, 200


def user_register_post(inline_object1=None):
    """user_register_post

    Регистрация нового пользователя

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
            with ConnectionFromPool() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO cdm.users (first_name, second_name, birthdate, biography, city, password_hash)"
                        "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                        (inline_object1.first_name, inline_object1.second_name, inline_object1.birthdate,
                         inline_object1.biography, inline_object1.city, password_hash)
                    )
                    user_id = cursor.fetchone()[0]
                    connection.commit()
                response = InlineResponse2001(user_id)
                return response, 200
    except Exception:
        response = InlineResponse500(message='Ошибка создания пользователя', code=500, request_id=request_id)
        return response, response.code


@jwt_required(fresh=True)
@jwt_user_in_database_required
def user_search_get(*args, **kwargs):
    """user_search_get

    Поиск анкет

    :rtype: User
    """
    request_id = str(time.time_ns()) + str(random.randint(1, 1000))
    try:
        # Доступ к параметрам запроса через объект request
        first_name = request.args.get('first_name')
        second_name = request.args.get('second_name')

        if not first_name or not second_name:
            return "Невалидные данные", 400

        result = get_user_info_from_database_search(first_name, second_name)
        if result is None:
            return "Пользователей не найдено", 200
        return result, 200
    except Exception:
        response = InlineResponse500(message='Ошибка поиска', code=500, request_id=request_id)
        return response, response.code
