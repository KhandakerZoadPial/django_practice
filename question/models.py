from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField(blank=True)
    # and all other fields


class Answer(models.Model):
    answer_of = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)