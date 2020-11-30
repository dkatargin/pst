import uuid

from mongoengine import Document, fields


# Create your models here.
class Post(Document):
    id = fields.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = fields.StringField()
