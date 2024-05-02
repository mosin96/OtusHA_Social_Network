import connexion
import six

from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.inline_response500 import InlineResponse500  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def login_post(inline_object=None):  # noqa: E501
    """login_post

    Упрощенный процесс аутентификации путем передачи идентификатор пользователя и получения токена для дальнейшего прохождения авторизации # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
    if connexion.request.is_json:
        inline_object1 = InlineObject1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
