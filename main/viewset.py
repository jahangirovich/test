
from .serializers import *
# Create your views here.
from rest_framework import generics,viewsets,views

class MyViewSets(viewsets.ModelViewSet):
    serializer_class = MyAnswerSerializer
    queryset = Answer.objects.all()

class Response(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()

# class RightAnswers(viewsets.ModelViewSet):
#     serializer_class = TrueSerializer
#     queryset = Right.objects.all()

class Quizes(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class Question(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class Test(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class Variant(viewsets.ModelViewSet):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()