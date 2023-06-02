from django.urls import path
from .views import *

urlpatterns = [
    path('fav/<int:id>/',favourite_add, name='favourite_add'),
    path('register/',UserRegisterView.as_view(), name='register'),
    path('Profile/',profile, name='profile'),
]

