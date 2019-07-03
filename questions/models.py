from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator
from django.template.defaultfilters import truncatechars
from enum import Enum
from django.contrib.auth.models import User

class stat(Enum):
     ve= 'Very easy'
     e= 'Easy'
     mod= 'Moderate'
     hard= 'Hard'
     Exp= 'Expert'

class Question(models.Model):
    name= RichTextField()
    @property
    def short_description(self):
       return truncatechars(self.description, 100)


class min_mark(models.Model):
    marks= models.IntegerField(validators=[MinValueValidator(10)])

class max_mark(models.Model):
    marks= models.IntegerField()
    
class difficulty(models.Model):
    level= models.CharField(max_length= 10, choices=[(tag, tag.value) for tag in stat])



class Topic(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ManyToManyField(Question)


    def __str__(self):
      return self.name



class Type(models.Model):
    name = models.CharField(max_length=50)
    parent= models.ForeignKey(Question, related_name='type', null=True, blank=True, on_delete= models.CASCADE)
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
    
    def __str__(self):
        return self.name   



class date(models.Model):
    date= models.DateField(auto_now_add=True)

class author(models.Model):
    designed_by= models.ForeignKey(User, related_name='+', on_delete= models.CASCADE)
     
