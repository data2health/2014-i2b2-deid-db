# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.annotation_source import AnnotationSource
from openapi_server.models.text_contact_annotation import TextContactAnnotation
from openapi_server.models.text_covid_symptom_annotation import TextCovidSymptomAnnotation
from openapi_server.models.text_date_annotation import TextDateAnnotation
from openapi_server.models.text_id_annotation import TextIdAnnotation
from openapi_server.models.text_person_name_annotation import TextPersonNameAnnotation
from openapi_server.models.text_physical_address_annotation import TextPhysicalAddressAnnotation
from openapi_server import util

from openapi_server.models.annotation_source import AnnotationSource  # noqa: E501
from openapi_server.models.text_contact_annotation import TextContactAnnotation  # noqa: E501
from openapi_server.models.text_covid_symptom_annotation import TextCovidSymptomAnnotation  # noqa: E501
from openapi_server.models.text_date_annotation import TextDateAnnotation  # noqa: E501
from openapi_server.models.text_id_annotation import TextIdAnnotation  # noqa: E501
from openapi_server.models.text_person_name_annotation import TextPersonNameAnnotation  # noqa: E501
from openapi_server.models.text_physical_address_annotation import TextPhysicalAddressAnnotation  # noqa: E501

class AnnotationCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, annotation_source=None, text_date_annotations=None, text_person_name_annotations=None, text_physical_address_annotations=None, text_id_annotations=None, text_contact_annotations=None, text_covid_symptom_annotations=None):  # noqa: E501
        """AnnotationCreateRequest - a model defined in OpenAPI

        :param annotation_source: The annotation_source of this AnnotationCreateRequest.  # noqa: E501
        :type annotation_source: AnnotationSource
        :param text_date_annotations: The text_date_annotations of this AnnotationCreateRequest.  # noqa: E501
        :type text_date_annotations: List[TextDateAnnotation]
        :param text_person_name_annotations: The text_person_name_annotations of this AnnotationCreateRequest.  # noqa: E501
        :type text_person_name_annotations: List[TextPersonNameAnnotation]
        :param text_physical_address_annotations: The text_physical_address_annotations of this AnnotationCreateRequest.  # noqa: E501
        :type text_physical_address_annotations: List[TextPhysicalAddressAnnotation]
        :param text_id_annotations: The text_id_annotations of this AnnotationCreateRequest.  # noqa: E501
        :type text_id_annotations: List[TextIdAnnotation]
        :param text_contact_annotations: The text_contact_annotations of this AnnotationCreateRequest.  # noqa: E501
        :type text_contact_annotations: List[TextContactAnnotation]
        :param text_covid_symptom_annotations: The text_covid_symptom_annotations of this AnnotationCreateRequest.  # noqa: E501
        :type text_covid_symptom_annotations: List[TextCovidSymptomAnnotation]
        """
        self.openapi_types = {
            'annotation_source': AnnotationSource,
            'text_date_annotations': List[TextDateAnnotation],
            'text_person_name_annotations': List[TextPersonNameAnnotation],
            'text_physical_address_annotations': List[TextPhysicalAddressAnnotation],
            'text_id_annotations': List[TextIdAnnotation],
            'text_contact_annotations': List[TextContactAnnotation],
            'text_covid_symptom_annotations': List[TextCovidSymptomAnnotation]
        }

        self.attribute_map = {
            'annotation_source': 'annotationSource',
            'text_date_annotations': 'textDateAnnotations',
            'text_person_name_annotations': 'textPersonNameAnnotations',
            'text_physical_address_annotations': 'textPhysicalAddressAnnotations',
            'text_id_annotations': 'textIdAnnotations',
            'text_contact_annotations': 'textContactAnnotations',
            'text_covid_symptom_annotations': 'textCovidSymptomAnnotations'
        }

        self._annotation_source = annotation_source
        self._text_date_annotations = text_date_annotations
        self._text_person_name_annotations = text_person_name_annotations
        self._text_physical_address_annotations = text_physical_address_annotations
        self._text_id_annotations = text_id_annotations
        self._text_contact_annotations = text_contact_annotations
        self._text_covid_symptom_annotations = text_covid_symptom_annotations

    @classmethod
    def from_dict(cls, dikt) -> 'AnnotationCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnnotationCreateRequest of this AnnotationCreateRequest.  # noqa: E501
        :rtype: AnnotationCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def annotation_source(self):
        """Gets the annotation_source of this AnnotationCreateRequest.


        :return: The annotation_source of this AnnotationCreateRequest.
        :rtype: AnnotationSource
        """
        return self._annotation_source

    @annotation_source.setter
    def annotation_source(self, annotation_source):
        """Sets the annotation_source of this AnnotationCreateRequest.


        :param annotation_source: The annotation_source of this AnnotationCreateRequest.
        :type annotation_source: AnnotationSource
        """
        if annotation_source is None:
            raise ValueError("Invalid value for `annotation_source`, must not be `None`")  # noqa: E501

        self._annotation_source = annotation_source

    @property
    def text_date_annotations(self):
        """Gets the text_date_annotations of this AnnotationCreateRequest.

        Date annotations in a text  # noqa: E501

        :return: The text_date_annotations of this AnnotationCreateRequest.
        :rtype: List[TextDateAnnotation]
        """
        return self._text_date_annotations

    @text_date_annotations.setter
    def text_date_annotations(self, text_date_annotations):
        """Sets the text_date_annotations of this AnnotationCreateRequest.

        Date annotations in a text  # noqa: E501

        :param text_date_annotations: The text_date_annotations of this AnnotationCreateRequest.
        :type text_date_annotations: List[TextDateAnnotation]
        """

        self._text_date_annotations = text_date_annotations

    @property
    def text_person_name_annotations(self):
        """Gets the text_person_name_annotations of this AnnotationCreateRequest.

        Person name annotations in a text  # noqa: E501

        :return: The text_person_name_annotations of this AnnotationCreateRequest.
        :rtype: List[TextPersonNameAnnotation]
        """
        return self._text_person_name_annotations

    @text_person_name_annotations.setter
    def text_person_name_annotations(self, text_person_name_annotations):
        """Sets the text_person_name_annotations of this AnnotationCreateRequest.

        Person name annotations in a text  # noqa: E501

        :param text_person_name_annotations: The text_person_name_annotations of this AnnotationCreateRequest.
        :type text_person_name_annotations: List[TextPersonNameAnnotation]
        """

        self._text_person_name_annotations = text_person_name_annotations

    @property
    def text_physical_address_annotations(self):
        """Gets the text_physical_address_annotations of this AnnotationCreateRequest.

        Physical address annotations in a text  # noqa: E501

        :return: The text_physical_address_annotations of this AnnotationCreateRequest.
        :rtype: List[TextPhysicalAddressAnnotation]
        """
        return self._text_physical_address_annotations

    @text_physical_address_annotations.setter
    def text_physical_address_annotations(self, text_physical_address_annotations):
        """Sets the text_physical_address_annotations of this AnnotationCreateRequest.

        Physical address annotations in a text  # noqa: E501

        :param text_physical_address_annotations: The text_physical_address_annotations of this AnnotationCreateRequest.
        :type text_physical_address_annotations: List[TextPhysicalAddressAnnotation]
        """

        self._text_physical_address_annotations = text_physical_address_annotations

    @property
    def text_id_annotations(self):
        """Gets the text_id_annotations of this AnnotationCreateRequest.

        ID annotations in a text  # noqa: E501

        :return: The text_id_annotations of this AnnotationCreateRequest.
        :rtype: List[TextIdAnnotation]
        """
        return self._text_id_annotations

    @text_id_annotations.setter
    def text_id_annotations(self, text_id_annotations):
        """Sets the text_id_annotations of this AnnotationCreateRequest.

        ID annotations in a text  # noqa: E501

        :param text_id_annotations: The text_id_annotations of this AnnotationCreateRequest.
        :type text_id_annotations: List[TextIdAnnotation]
        """

        self._text_id_annotations = text_id_annotations

    @property
    def text_contact_annotations(self):
        """Gets the text_contact_annotations of this AnnotationCreateRequest.

        Contact annotations in a text  # noqa: E501

        :return: The text_contact_annotations of this AnnotationCreateRequest.
        :rtype: List[TextContactAnnotation]
        """
        return self._text_contact_annotations

    @text_contact_annotations.setter
    def text_contact_annotations(self, text_contact_annotations):
        """Sets the text_contact_annotations of this AnnotationCreateRequest.

        Contact annotations in a text  # noqa: E501

        :param text_contact_annotations: The text_contact_annotations of this AnnotationCreateRequest.
        :type text_contact_annotations: List[TextContactAnnotation]
        """

        self._text_contact_annotations = text_contact_annotations

    @property
    def text_covid_symptom_annotations(self):
        """Gets the text_covid_symptom_annotations of this AnnotationCreateRequest.

        COVID symptom annotations in a text  # noqa: E501

        :return: The text_covid_symptom_annotations of this AnnotationCreateRequest.
        :rtype: List[TextCovidSymptomAnnotation]
        """
        return self._text_covid_symptom_annotations

    @text_covid_symptom_annotations.setter
    def text_covid_symptom_annotations(self, text_covid_symptom_annotations):
        """Sets the text_covid_symptom_annotations of this AnnotationCreateRequest.

        COVID symptom annotations in a text  # noqa: E501

        :param text_covid_symptom_annotations: The text_covid_symptom_annotations of this AnnotationCreateRequest.
        :type text_covid_symptom_annotations: List[TextCovidSymptomAnnotation]
        """

        self._text_covid_symptom_annotations = text_covid_symptom_annotations
