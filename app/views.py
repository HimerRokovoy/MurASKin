from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .import models
# Create your views here.


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context = context)

def question(request, question_id : int):
    question_item = models.QUESTIONS[question_id]
    context = {'question': question_item}
    return render(request, 'question.html', context = context)

