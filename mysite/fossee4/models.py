from django.db import models
from .validators import validate_file_size

# Create your models here.

# model called ‘Images’ with ‘id’, ‘name’, ‘description’, ‘image’, ‘createdby’. 
class Images(models.Model):
    ide = models.IntegerField(default = 0) # id can also be generated using pk.
    name = models.CharField(max_length = 80)
    description = models.TextField(default = ' ')
    image = models.ImageField(upload_to = 'images/',validators=[validate_file_size])
    createdby = models.CharField(max_length = 80)