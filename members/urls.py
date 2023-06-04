from django.urls import path
from .views import *

urlpatterns = [
    path('fav/<int:id>/',favourite_add, name='favourite_add'),
    path('register/',UserRegisterView.as_view(), name='register'),
    path('Profile/',profile, name='profile'),
    path('settings/',SettingsView.as_view(), name='settings'),
    path('settings/password/',PasswordsChangeView.as_view(template_name='registration/change-password.html'),name='change_pass'),
]

