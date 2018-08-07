from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Quiz(models.Model):

    title = models.CharField(max_length=60,blank=False,)
    points = models.IntegerField()

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


    def __unicode__(self):
        return self.title

    def __str__(self):
        return "%s"%self.title

class Variant(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    number = models.IntegerField(blank=True)
    def __str__(self):
        return "%s"%self.number

class Question(models.Model):

    quiz = models.ForeignKey(Variant,on_delete=models.CASCADE)
    objects = models.Manager()

    content = models.TextField(blank=False, verbose_name='Question',)

    TYPES = (
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
        ('text', 'text'),
    )

    type = models.CharField(max_length=8, choices=TYPES, default='radio')

    language_code = 'en'
    translated_fields = ['content', 'feedback']
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        #ordering = ['category']

    def __unicode__(self):
        return self.content
    def __str__(self):
        return "%s"%self.content

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    q = models.TextField(blank=True)
    content = models.CharField(max_length=1000, blank=False,)
    correct = models.BooleanField(blank=False, default=False,help_text="Это правильный ответ?")
    translated_fields = ['content']
    def __unicode__(self):
        return "%s"%self.content
    def __str__(self):
        return "%s and "%self.content

class Response(models.Model):
    quiz = models.ForeignKey(Variant,on_delete=models.CASCADE,blank=True)
    answer = models.IntegerField(blank=True)
    date = models.DateField(default=date.today(),blank=True)
    username = models.CharField(max_length=100,blank=True)
    quizes = models.TextField(blank=True)
    notright = models.IntegerField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)



class Test(models.Model):
    right = models.TextField(blank=True)
    false = models.TextField(blank=True)
    question = models.TextField(blank=True)
    response = models.ForeignKey(Response,on_delete=models.CASCADE)
