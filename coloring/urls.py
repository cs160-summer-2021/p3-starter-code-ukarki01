from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('index', views.index, name='index'),
    path('new_interaction', views.new_interaction, name='new_interaction')
]
