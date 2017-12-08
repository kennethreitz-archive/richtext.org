from django.db import models

# Create your models here.
class RichPost(models.Model):
    text = models.TextField()
    views = models.BigIntegerField()
    published = models.DateTimeField('date published')