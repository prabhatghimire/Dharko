from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=140)
    detail=models.TextField(max_length=140)
    body = models.FileField()


    def __str__(self):
        return self.title


class About(models.Model):
    detail=models.TextField(max_length=14000)


    def __str__(self):
        return self.detail