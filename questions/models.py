from django.db import models
from django.contrib.auth.models import User

class questions(models.Model):
    name= models.CharField(max_length=255)
    relation= models.ManyToManyField('self')

class Topic(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
       return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name

class creator(models.Model):
     user= models.CharField(max_length=50)
     designed_by= models.ForeignKey('self', on_delete= models.CASCADE)

