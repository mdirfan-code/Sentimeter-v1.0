from django.db import models

class TwitterHash(models.Model):
  hashTag = models.CharField(max_length=120)
  
  def __str__(self):
    return self.hashTag