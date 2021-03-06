from mongoengine import StringField, EmbeddedDocument


class ResourceSource(EmbeddedDocument):
    name = StringField(required=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
