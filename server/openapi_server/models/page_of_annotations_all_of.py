# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
# from openapi_server.models.any_of_stored_annotation_stored_date_annotation import AnyOfStoredAnnotationStoredDateAnnotation
from openapi_server import util

# from openapi_server.models.any_of_stored_annotation_stored_date_annotation import AnyOfStoredAnnotationStoredDateAnnotation  # noqa: E501

class PageOfAnnotationsAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, items=None):  # noqa: E501
        """PageOfAnnotationsAllOf - a model defined in OpenAPI

        :param items: The items of this PageOfAnnotationsAllOf.  # noqa: E501
        :type items: List[AnyOfStoredAnnotationStoredDateAnnotation]
        """
        self.openapi_types = {
            'items': List[AnyOfStoredAnnotationStoredDateAnnotation]
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfAnnotationsAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfAnnotations_allOf of this PageOfAnnotationsAllOf.  # noqa: E501
        :rtype: PageOfAnnotationsAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this PageOfAnnotationsAllOf.

        An array of annotations  # noqa: E501

        :return: The items of this PageOfAnnotationsAllOf.
        :rtype: List[AnyOfStoredAnnotationStoredDateAnnotation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageOfAnnotationsAllOf.

        An array of annotations  # noqa: E501

        :param items: The items of this PageOfAnnotationsAllOf.
        :type items: List[AnyOfStoredAnnotationStoredDateAnnotation]
        """

        self._items = items
