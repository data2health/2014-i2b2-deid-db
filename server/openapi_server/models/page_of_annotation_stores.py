# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.annotation_store import AnnotationStore
from openapi_server.models.page_of_annotation_stores_all_of import PageOfAnnotationStoresAllOf
from openapi_server.models.page_response import PageResponse
from openapi_server.models.page_response_links import PageResponseLinks
from openapi_server import util

from openapi_server.models.annotation_store import AnnotationStore  # noqa: E501
from openapi_server.models.page_of_annotation_stores_all_of import PageOfAnnotationStoresAllOf  # noqa: E501
from openapi_server.models.page_response import PageResponse  # noqa: E501
from openapi_server.models.page_response_links import PageResponseLinks  # noqa: E501

class PageOfAnnotationStores(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, items=None):  # noqa: E501
        """PageOfAnnotationStores - a model defined in OpenAPI

        :param offset: The offset of this PageOfAnnotationStores.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfAnnotationStores.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfAnnotationStores.  # noqa: E501
        :type links: PageResponseLinks
        :param items: The items of this PageOfAnnotationStores.  # noqa: E501
        :type items: List[AnnotationStore]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': PageResponseLinks,
            'items': List[AnnotationStore]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'items': 'items'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfAnnotationStores':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfAnnotationStores of this PageOfAnnotationStores.  # noqa: E501
        :rtype: PageOfAnnotationStores
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfAnnotationStores.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfAnnotationStores.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfAnnotationStores.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfAnnotationStores.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfAnnotationStores.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfAnnotationStores.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfAnnotationStores.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfAnnotationStores.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfAnnotationStores.


        :return: The links of this PageOfAnnotationStores.
        :rtype: PageResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfAnnotationStores.


        :param links: The links of this PageOfAnnotationStores.
        :type links: PageResponseLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def items(self):
        """Gets the items of this PageOfAnnotationStores.

        An array of annotation stores  # noqa: E501

        :return: The items of this PageOfAnnotationStores.
        :rtype: List[AnnotationStore]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageOfAnnotationStores.

        An array of annotation stores  # noqa: E501

        :param items: The items of this PageOfAnnotationStores.
        :type items: List[AnnotationStore]
        """

        self._items = items
