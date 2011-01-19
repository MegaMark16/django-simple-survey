import hashlib
import datetime

from django.db import models
from django.contrib.auth.models import User, Group

class Survey(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
class Question(models.Model):
    question = models.TextField()
    survey = models.ForeignKey(Survey)
    
    def __unicode__(self):
        return self.question

class Response(models.Model):
	survey = models.ForeignKey(Survey)

class Answer(models.Model):
    answer = models.TextField()
    response = models.ForeignKey(Response)
    question = models.ForeignKey(Question)
        
    def __unicode__(self):
        return self.answer
