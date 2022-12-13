from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .import models
# Create your views here.


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context = context)

def question(request, question_id : int):
    context = {'question': models.QUESTIONS[question_id]}
    return render(request, 'question.html', context = context)
    
def tag(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'tag.html', context = context)

def login(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'login.html', context = context)

def signup(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'signup.html', context = context)

def ask(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'ask.html', context = context)

def settings(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'settings.html', context = context)

    

