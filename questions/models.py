from django.db import models

# Create your models here.
class Topic(models.Model):
	name=models.CharField(max_length=50)
	parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
	def __str__(self):
		return self.name
	
    
