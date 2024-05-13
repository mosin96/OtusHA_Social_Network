from typing import List

import jwt
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request


def info_from_bearerAuth(token):
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    try:
        verify_jwt_in_request(fresh=True)
        sub = get_jwt_identity()
        return {'uid': sub}
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
