from django.db import models
from django.contrib.auth.models import User

class questions(models.Model):
    name= models.CharField(max_length=255)
    relation= models.ManyToManyField('self')

class creator(models.Model):
     user= models.CharField(max_length=50)
     designed_by= models.ForeignKey('self', on_delete= models.CASCADE)
