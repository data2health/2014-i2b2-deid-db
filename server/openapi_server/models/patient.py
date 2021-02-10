# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class Patient(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identifier=None, gender=None):  # noqa: E501
        """Patient - a model defined in OpenAPI

        :param identifier: The identifier of this Patient.  # noqa: E501
        :type identifier: str
        :param gender: The gender of this Patient.  # noqa: E501
        :type gender: str
        """
        self.openapi_types = {
            'identifier': str,
            'gender': str
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'gender': 'gender'
        }

        self._identifier = identifier
        self._gender = gender

    @classmethod
    def from_dict(cls, dikt) -> 'Patient':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Patient of this Patient.  # noqa: E501
        :rtype: Patient
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self):
        """Gets the identifier of this Patient.

        The ID of the FHIR patient  # noqa: E501

        :return: The identifier of this Patient.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Patient.

        The ID of the FHIR patient  # noqa: E501

        :param identifier: The identifier of this Patient.
        :type identifier: str
        """
        if identifier is not None and len(identifier) > 60:
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `60`")  # noqa: E501
        if identifier is not None and len(identifier) < 3:
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `3`")  # noqa: E501
        if identifier is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', identifier):  # noqa: E501
            raise ValueError("Invalid value for `identifier`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._identifier = identifier

    @property
    def gender(self):
        """Gets the gender of this Patient.

        Gender of the patient  # noqa: E501

        :return: The gender of this Patient.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Patient.

        Gender of the patient  # noqa: E501

        :param gender: The gender of this Patient.
        :type gender: str
        """
        allowed_values = ["male", "female", "other", "unknown"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender
