from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question_t=models.CharField(max_length=100,unique=True)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_t

    def was_published_recently(self):
        time=timezone.now()
        return self.pub_date <= time

class Choice(models.Model):
    choice_t=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_t
