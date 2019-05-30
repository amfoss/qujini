from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length = 50)
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name
