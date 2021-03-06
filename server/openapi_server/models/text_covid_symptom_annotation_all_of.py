# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TextCovidSymptomAnnotationAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, condition=None, certainty=None):  # noqa: E501
        """TextCovidSymptomAnnotationAllOf - a model defined in OpenAPI

        :param condition: The condition of this TextCovidSymptomAnnotationAllOf.  # noqa: E501
        :type condition: str
        :param certainty: The certainty of this TextCovidSymptomAnnotationAllOf.  # noqa: E501
        :type certainty: str
        """
        self.openapi_types = {
            'condition': str,
            'certainty': str
        }

        self.attribute_map = {
            'condition': 'condition',
            'certainty': 'certainty'
        }

        self._condition = condition
        self._certainty = certainty

    @classmethod
    def from_dict(cls, dikt) -> 'TextCovidSymptomAnnotationAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextCovidSymptomAnnotation_allOf of this TextCovidSymptomAnnotationAllOf.  # noqa: E501
        :rtype: TextCovidSymptomAnnotationAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def condition(self):
        """Gets the condition of this TextCovidSymptomAnnotationAllOf.

        The sign/symptom type according to CDC definition   # noqa: E501

        :return: The condition of this TextCovidSymptomAnnotationAllOf.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this TextCovidSymptomAnnotationAllOf.

        The sign/symptom type according to CDC definition   # noqa: E501

        :param condition: The condition of this TextCovidSymptomAnnotationAllOf.
        :type condition: str
        """
        allowed_values = ["fever", "chill", "cough", "fatigue", "nasal_obstruction", "loss_of_appetite", "diarrhea", "abdominal_pain", "nausea", "vomiting", "sore_throat", "headache", "myalgia", "loss_of_taste", "loss_of_smell", "dyspnea", "chest_pain", "delirium", "hypersomnia", "cyanosis"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def certainty(self):
        """Gets the certainty of this TextCovidSymptomAnnotationAllOf.

        Whether the annotation is positively or negatively correlated with the presence of COVID   # noqa: E501

        :return: The certainty of this TextCovidSymptomAnnotationAllOf.
        :rtype: str
        """
        return self._certainty

    @certainty.setter
    def certainty(self, certainty):
        """Sets the certainty of this TextCovidSymptomAnnotationAllOf.

        Whether the annotation is positively or negatively correlated with the presence of COVID   # noqa: E501

        :param certainty: The certainty of this TextCovidSymptomAnnotationAllOf.
        :type certainty: str
        """
        allowed_values = ["positive", "negated", "possible"]  # noqa: E501
        if certainty not in allowed_values:
            raise ValueError(
                "Invalid value for `certainty` ({0}), must be one of {1}"
                .format(certainty, allowed_values)
            )

        self._certainty = certainty
