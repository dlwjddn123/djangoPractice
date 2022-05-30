from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.create, name = 'create'),
    path('test/', views.test, name="test"),
    path('grade/', views.grade, name="grade"),
    path('result/', views.result, name='result')
]