from django.db import models

class Url(models.Model):
    link = models.CharField(max_length=10000, default='')
    uuid = models.CharField(max_length=10)