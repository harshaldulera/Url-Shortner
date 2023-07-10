from django.db import models

class Url(models.Model):
    link = models.CharField(max_length=10000),
models.CharField(max_length=10)