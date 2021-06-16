from django.db import models

# Create your models here.
from django.db import models


class Order(models.Model):
    state = models.CharField(max_length=32)

