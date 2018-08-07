from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import DeleteView,CreateView
from django.views import View
from .serializers import *
# Create your views here.
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics,viewsets,views
from django.contrib import messages
from django.contrib.auth.decorators import *
from django.db.models import Q

@login_required
def indexView(request):
    queryset = Quiz.objects.all()
    return render(request,'main.html',{'queryset':queryset})

@login_required
def choose(request,pk):
    quiz = get_object_or_404(Quiz,pk=pk)
    variants = Variant.objects.all().filter(quiz=quiz)
    return render(request,'choose.html',{'variants':variants})

@login_required
def DetailView(request,pk):
    query = get_object_or_404(Variant,pk=pk)
    question = Question.objects.all().filter(quiz=query)
    current_user = request.user
    return render(request,'tests.html',{'question':question,'user':current_user.id,'i':pk,'use':current_user,'quiz':query})

@login_required
def Administration(request):
    quiz = Quiz.objects.all()
    form = QuizForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/main/administration/')
    return render(request,'administration.html',{'quiz':quiz,'form':form})

@login_required
def Variants(request,pk):
    quiz = get_object_or_404(Quiz,pk=pk)
    variants = Variant.objects.all().filter(quiz=quiz)
    if request.POST:
        form = VariantForm(data=request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.quiz = quiz
            temp.save()
            return redirect('/main/variant/' + pk +'/')
    else:
        form = VariantForm()
    return render(request,'variant.html',{'form':form,'quiz':quiz,'variants':variants})

@login_required
def Questions(request,pk):
    quiz = get_object_or_404(Variant,pk=pk)
    questions = Question.objects.all().filter(quiz=quiz)
    if request.POST:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.quiz = quiz
            temp.save()
            return redirect('/main/question/' + pk + '/')
    else:
        form = QuestionForm()
    return render(request,'questions.html',{'questions':questions,'form':form,'quiz':quiz,'pk':pk})

@login_required
def Answers(request,pk):
    question = get_object_or_404(Question,pk=pk)
    answers = Answer.objects.all().filter(question=question)
    if request.POST:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.question = question
            temp.q = question
            temp.save()
            return redirect('/main/answers/' + pk + '/')
    else:
        form = AnswerForm()
    return render(request,'many_answers.html',{'form':form,'answers':answers,'question':question})

@login_required
def allAnswers(request):
    return render(request,'answers.html')

@login_required
def results(request):
    results = Response.objects.all().filter(user=request.user)
    return render(request,'results.html',{'results':results})

@login_required
def admin_results(request):
    query = request.GET.get('q')
    queryset_list = Response.objects.all()
    if query:
        queryset_list = queryset_list.filter(
            Q(username__icontains=query)
        ).distinct()
    return render(request,'search.html',{'queryset':queryset_list})

@login_required
def list(request,pk):
    onme = get_object_or_404(Response,pk=pk)
    queryset = Test.objects.all().filter(response=onme)
    return render(request,'detail.html',{'queryset':queryset,'on':onme})
