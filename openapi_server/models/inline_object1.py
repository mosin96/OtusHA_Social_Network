# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, first_name=None, second_name=None, birthdate=None, biography=None, city=None, password=None):  # noqa: E501
        """InlineObject1 - a model defined in OpenAPI

        :param first_name: The first_name of this InlineObject1.  # noqa: E501
        :type first_name: str
        :param second_name: The second_name of this InlineObject1.  # noqa: E501
        :type second_name: str
        :param birthdate: The birthdate of this InlineObject1.  # noqa: E501
        :type birthdate: date
        :param biography: The biography of this InlineObject1.  # noqa: E501
        :type biography: str
        :param city: The city of this InlineObject1.  # noqa: E501
        :type city: str
        :param password: The password of this InlineObject1.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'first_name': str,
            'second_name': str,
            'birthdate': date,
            'biography': str,
            'city': str,
            'password': str
        }

        self.attribute_map = {
            'first_name': 'first_name',
            'second_name': 'second_name',
            'birthdate': 'birthdate',
            'biography': 'biography',
            'city': 'city',
            'password': 'password'
        }

        self._first_name = first_name
        self._second_name = second_name
        self._birthdate = birthdate
        self._biography = biography
        self._city = city
        self._password = password

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_1 of this InlineObject1.  # noqa: E501
        :rtype: InlineObject1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self):
        """Gets the first_name of this InlineObject1.


        :return: The first_name of this InlineObject1.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InlineObject1.


        :param first_name: The first_name of this InlineObject1.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def second_name(self):
        """Gets the second_name of this InlineObject1.


        :return: The second_name of this InlineObject1.
        :rtype: str
        """
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        """Sets the second_name of this InlineObject1.


        :param second_name: The second_name of this InlineObject1.
        :type second_name: str
        """

        self._second_name = second_name

    @property
    def birthdate(self):
        """Gets the birthdate of this InlineObject1.

        Дата рождения  # noqa: E501

        :return: The birthdate of this InlineObject1.
        :rtype: date
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        """Sets the birthdate of this InlineObject1.

        Дата рождения  # noqa: E501

        :param birthdate: The birthdate of this InlineObject1.
        :type birthdate: date
        """

        self._birthdate = birthdate

    @property
    def biography(self):
        """Gets the biography of this InlineObject1.


        :return: The biography of this InlineObject1.
        :rtype: str
        """
        return self._biography

    @biography.setter
    def biography(self, biography):
        """Sets the biography of this InlineObject1.


        :param biography: The biography of this InlineObject1.
        :type biography: str
        """

        self._biography = biography

    @property
    def city(self):
        """Gets the city of this InlineObject1.


        :return: The city of this InlineObject1.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this InlineObject1.


        :param city: The city of this InlineObject1.
        :type city: str
        """

        self._city = city

    @property
    def password(self):
        """Gets the password of this InlineObject1.


        :return: The password of this InlineObject1.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineObject1.


        :param password: The password of this InlineObject1.
        :type password: str
        """

        self._password = password