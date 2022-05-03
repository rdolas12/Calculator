from django.urls import path, include
from . import views

urlpatterns = [
    path('Add/', views.addnum, name='add'),
    path('Sub/', views.subnum,name='sub'),
]
