from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField


class Topic(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name


class Question(models.Model):
    VeryEasy = 'Very Easy'
    Easy = 'Easy'
    Moderate = 'Moderate'
    Expert = 'Expert'
    difficulty_choices = [
        (VeryEasy, 'VeryEasy'),
        (Easy, 'Easy'),
        (Moderate, 'Moderate'),
        (Expert, 'Expert'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    min_mark = models.IntegerField()
    max_mark = models.IntegerField(null=True)
    difficulty = models.CharField(
        max_length=20,
        choices=difficulty_choices,
        default=VeryEasy
    )
    date = models.DateField()
    questionType = models.ForeignKey(Type, on_delete=models.CASCADE)
    question = RichTextField(blank=True, null=True)
    topic = models.ManyToManyField(Topic)

    def mark_range(self):
        return '{}-{}'.format(self.min_mark, self.max_mark)

    def get_topics(self):
        return "\n".join([p.name for p in self.topic.all()])

    @property
    def question_trim(self):
        return truncatechars(self.question, 100)
