from django.test import TestCase
from django.utils import timezone
import datetime
from .models import *
from django.urls import reverse
from django.test import Client

# Create your tests here.
"""
class QuestionModelsTests(TestCase):
    #to test whether all of questions are in the past andnot in future_question
    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        """
def create_question(question_t,days):
    time=timezone.now()+datetime.timedelta(days)
    #to create a class in past or future,days can be postive for future and negative for past
    return Question.objects.create(question_t=question_t,pub_date=time)

class QuestionIndexTest(TestCase):
    def test_no_questions(self):
        response=self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No questions available")

    def test_past_question(self):
        create_question(question_t="past question",days=-30)
        response=self.client.get(reverse('polls:index'))
        #self.assertEqual(response.context['ques_list'],<QuerySet [<Question: past question>]>)
        #self.assertEqual(response.context['ques_list'],'<QuerySet [<Question: past question>]>')
