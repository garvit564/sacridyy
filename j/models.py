# models.py
from django.db import models



class ImageModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    
  

class WriteModel(models.Model):
    text = models.CharField(max_length=1000)    

    def __str__(self):
        return self.text


