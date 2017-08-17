from django.db import models
# Create your models here.


class Work(models.Model):
    email = models.URLField(max_length=64)
    name = models.CharField(max_length=64)
    post = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Study(models.Model):
    email = models.URLField(max_length=64)
    name = models.CharField(max_length=64)
    post = models.CharField(max_length=64)

    def __str__(self):
        return self.name
