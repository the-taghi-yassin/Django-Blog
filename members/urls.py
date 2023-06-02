from django.urls import path
from .views import *

urlpatterns = [
    path('fav/<int:id>/',favourite_add, name='favourite_add'),
    path('register/',UserRegisterView.as_view(), name='register'),
    path('Profile/',profile, name='profile'),
    path('Profile_edit/',ProfileEditView.as_view(), name='profile-edit'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
]

