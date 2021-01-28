# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.annotation import Annotation  # noqa: E501
from openapi_server.models.response_page_metadata import ResponsePageMetadata  # noqa: E501
from openapi_server.models.response_page_metadata_links import ResponsePageMetadataLinks  # noqa: E501
from openapi_server import util


class PageOfAnnotations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=0, limit=10, links=None, annotations=None):  # noqa: E501
        """PageOfAnnotations - a model defined in OpenAPI

        :param offset: The offset of this PageOfAnnotations.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfAnnotations.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfAnnotations.  # noqa: E501
        :type links: ResponsePageMetadataLinks
        :param annotations: The annotations of this PageOfAnnotations.  # noqa: E501
        :type annotations: List[Annotation]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ResponsePageMetadataLinks,
            'annotations': List[Annotation]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'annotations': 'annotations'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._annotations = annotations

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfAnnotations':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfAnnotations of this PageOfAnnotations.  # noqa: E501
        :rtype: PageOfAnnotations
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfAnnotations.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfAnnotations.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfAnnotations.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfAnnotations.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501
        if offset is not None and offset < 0:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfAnnotations.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfAnnotations.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfAnnotations.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfAnnotations.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501
        if limit is not None and limit > 100:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `100`")  # noqa: E501
        if limit is not None and limit < 10:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `10`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfAnnotations.


        :return: The links of this PageOfAnnotations.
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfAnnotations.


        :param links: The links of this PageOfAnnotations.
        :type links: ResponsePageMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def annotations(self):
        """Gets the annotations of this PageOfAnnotations.

        An array of annotations  # noqa: E501

        :return: The annotations of this PageOfAnnotations.
        :rtype: List[Annotation]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this PageOfAnnotations.

        An array of annotations  # noqa: E501

        :param annotations: The annotations of this PageOfAnnotations.
        :type annotations: List[Annotation]
        """

        self._annotations = annotations
