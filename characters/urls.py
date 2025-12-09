
from django.urls import path
from . import views

urlpatterns = [
path('home/', views.home, name='home'),
path('personatge<int:id>/', views.personatge, name='personatge'),
]