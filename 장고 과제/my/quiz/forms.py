from cProfile import label
from django import forms
from django.forms import ModelForm
from .models import Person, Quiz
 
class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        labels = {
            'quiznum' : "문제 번호",
            'description' : '문제',
            'choice1' : "1번",
            'choice2' : "2번",
            'choice3' : "3번",
            'choice4' : "4번",
            'choice5' : "5번",
            'answer' : "정답",
        }

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'