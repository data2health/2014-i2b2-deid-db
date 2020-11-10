# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.note_store import NoteStore
from openapi_server.models.page_of_note_stores_all_of import PageOfNoteStoresAllOf
from openapi_server.models.page_response import PageResponse
from openapi_server.models.page_response_links import PageResponseLinks
from openapi_server import util

from openapi_server.models.note_store import NoteStore  # noqa: E501
from openapi_server.models.page_of_note_stores_all_of import PageOfNoteStoresAllOf  # noqa: E501
from openapi_server.models.page_response import PageResponse  # noqa: E501
from openapi_server.models.page_response_links import PageResponseLinks  # noqa: E501

class PageOfNoteStores(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, items=None):  # noqa: E501
        """PageOfNoteStores - a model defined in OpenAPI

        :param offset: The offset of this PageOfNoteStores.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfNoteStores.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfNoteStores.  # noqa: E501
        :type links: PageResponseLinks
        :param items: The items of this PageOfNoteStores.  # noqa: E501
        :type items: List[NoteStore]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': PageResponseLinks,
            'items': List[NoteStore]
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
    def from_dict(cls, dikt) -> 'PageOfNoteStores':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfNoteStores of this PageOfNoteStores.  # noqa: E501
        :rtype: PageOfNoteStores
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfNoteStores.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfNoteStores.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfNoteStores.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfNoteStores.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfNoteStores.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfNoteStores.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfNoteStores.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfNoteStores.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfNoteStores.


        :return: The links of this PageOfNoteStores.
        :rtype: PageResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfNoteStores.


        :param links: The links of this PageOfNoteStores.
        :type links: PageResponseLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def items(self):
        """Gets the items of this PageOfNoteStores.

        An array of note stores  # noqa: E501

        :return: The items of this PageOfNoteStores.
        :rtype: List[NoteStore]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PageOfNoteStores.

        An array of note stores  # noqa: E501

        :param items: The items of this PageOfNoteStores.
        :type items: List[NoteStore]
        """

        self._items = items