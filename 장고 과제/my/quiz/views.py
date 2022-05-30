from django.shortcuts import render, redirect
from .models import *
from .forms import QuizForm


def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method=='POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizForm()
    return render(request, 'new.html', {'form': form})

def test(request):
    if request.method=='POST':
        form = Person()
        form.name = request.POST.get("description")
        form.std_num = request.POST.get("std_num")
        form.user_answers = request.POST.getlist("user_answers[]")
        form.save()
        if form.is_valid():
            form.save()
        return redirect('test')
    else:
        form = Quiz.objects.all()
    return render(request, 'start_test.html', {'form': form})

def grade(request):
    if request.method=='POST':
        user = Person.objects.all()
        form = Quiz.objects.all()
        if form.is_valid():
            form.save()
        return redirect('test')
    else:
        form = Quiz.objects.all()
    return render(request, 'grade.html', {'form': form, 'user':user})

def result(request):
    return redirect("home")