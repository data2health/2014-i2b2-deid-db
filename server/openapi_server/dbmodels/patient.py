from mongoengine import StringField

from openapi_server.dbmodels.base_document import BaseDocument


class Patient(BaseDocument):
    resourceName = StringField(required=True, unique=True)
    fhirStoreName = StringField()
    identifier = StringField()
    gender = StringField()

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        # doc["id"] = str(self.pk)

        # remove internal properties
        del doc['resourceName']
        del doc['fhirStoreName']

        return doc
