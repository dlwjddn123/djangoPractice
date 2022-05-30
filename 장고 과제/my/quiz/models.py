from django.db import models

class Quiz(models.Model):
    quiznum = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    choice5 = models.CharField(max_length=200)
    answer = models.IntegerField()
    

class Person(models.Model):
    name = models.CharField(max_length=200)
    std_num = models.CharField(max_length=200)
    score = models.IntegerField()
    user_answer = models.IntegerField()
    quiz_num = models.IntegerField()

     
     