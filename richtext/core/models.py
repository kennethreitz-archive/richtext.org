import uuid
from django.db import models

# Create your models here.
class RichPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    views = models.BigIntegerField()
    published = models.DateTimeField('date published')
    
    def __str__(self):
        return "<RichPost id='{}'>".format(self.id)