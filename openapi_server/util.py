import datetime
import uuid

import six
import typing

from flask_jwt_extended import get_jwt_identity

from openapi_server import typing_utils
from openapi_server.database.connection import get_db_connection


def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool, bytearray):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif typing_utils.is_generic(klass):
        if typing_utils.is_list(klass):
            return _deserialize_list(data, klass.__args__[0])
        if typing_utils.is_dict(klass):
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return an original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.openapi_types:
        return data

    for attr, attr_type in six.iteritems(instance.openapi_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}


# Метод для извлечения информации о пользователе из базы данных PostgreSQL
def get_user_info_from_database(user_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT biography, birthdate, city, first_name, id, second_name"
                " FROM cdm.users WHERE id = %s", (user_id,))
    user_info = cur.fetchone()

    cur.close()
    conn.close()

    if user_info:
        user = {'biography': user_info[0],
                'birthdate': user_info[1],
                'city': user_info[2],
                'first_name': user_info[3],
                'id': user_info[4],
                'second_name': user_info[5]}
        return user
    else:
        return None


def is_valid_uuid(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False


# Декоратор для проверки наличия пользователя в базе данных
def jwt_user_in_database_required(fn):
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT id FROM cdm.users "
                    f"WHERE id=\'{user_id}\'")
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return fn(*args, **kwargs)
        else:
            return "Токен выдан несуществующему пользователю", 401
    return wrapper
