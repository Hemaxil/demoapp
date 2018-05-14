from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
import datetime
from django.core.exceptions import *
# Create your views here.
def index(request):
    ques_list=Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
#    output='\n'.join([x.question_t for x in ques_list])
    return render(request,'polls/index.html',{'ques_list':ques_list})

def details(request,question_id):
    ques=get_object_or_404(Question,pk=question_id)
    #ques=Question.objects.get(pk=question_id)
    return render(request,'polls/details.html',{'ques':ques})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    selected_choice=question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes+=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=[question.id]))
