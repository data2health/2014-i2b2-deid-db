# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.fhir_store import FhirStore  # noqa: E501
from openapi_server.models.fhir_stores import FhirStores  # noqa: E501
from openapi_server.test import BaseTestCase


class TestFhirStoreController(BaseTestCase):
    """FhirStoreController integration test stubs"""

    def test_create_fhir_store(self):
        """Test case for create_fhir_store

        Create a FHIR store
        """
        fhir_store = {
  "name" : "name"
}
        query_string = [('fhirStoreId', awesome-fhir-store)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores'.format(dataset_id='dataset_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(fhir_store),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_fhir_store(self):
        """Test case for delete_fhir_store

        Delete a FHIR store
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fhir_store(self):
        """Test case for get_fhir_store

        Get a FHIR store
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores/{fhir_store_id}'.format(dataset_id='dataset_id_example', fhir_store_id='fhir_store_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_fhir_stores(self):
        """Test case for list_fhir_stores

        List the FHIR stores in a dataset
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/fhirStores'.format(dataset_id='dataset_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()