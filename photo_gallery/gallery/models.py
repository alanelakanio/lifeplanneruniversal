from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    country=models.CharField(max_length=255,null=True,blank=True)
    content=models.TextField(null=True,blank=True)
