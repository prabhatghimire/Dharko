from django.db import models



# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField()
    detail=models.TextField(max_length=140)
    body = models.FileField()


    def __str__(self):
        return self.title
