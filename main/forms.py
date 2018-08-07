from django import forms
from .models import *

class QuizForm(forms.ModelForm):
    title = forms.CharField(max_length=60,label='Заголовок')
    points = forms.IntegerField(label='Проходной балл')
    class Meta:
        model = Quiz
        fields = "__all__"

class QuestionForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,label='Вопросы')
    class Meta:
       model = Question
       fields = ('content',)

class AnswerForm(forms.ModelForm):
    content = forms.CharField(max_length=1000,label='Контент')
    correct = forms.BooleanField(label='Ваш ответ является правильным?',required=False)
    class Meta:
        model = Answer
        fields = ('content','correct')

class VariantForm(forms.ModelForm):
    number = forms.IntegerField(label='Номер Варианта')
    class Meta:
        model = Variant
        fields = ('number',)