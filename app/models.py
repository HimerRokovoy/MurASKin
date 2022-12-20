import django.contrib.auth.models
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.contrib.auth.models import User





class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default = "static/img/images.png")
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=50)
    unique = models.BooleanField(default = True)

    def __str__(self):
        return self.name


class Like(models.Model):
    author = models.ForeignKey(Profile, null = True, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)


class QuestionManager(models.Manager):
    def best(self):
        return self.filter.order_by('rating')
    
    

class Question(models.Model):
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text= models.TextField()
    tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)
    answers_num = models.IntegerField(default = 0)
    like =  models.ForeignKey(Like,null = True, blank = True, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0, null = False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.OneToOneField(Profile,on_delete=models.CASCADE)
    text = models.TextField()
    correctness = models.BooleanField(default = False)
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0, null = False)


    def __str__(self):
        return self.text
