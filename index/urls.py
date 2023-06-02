from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('add-article', AddCourseView.as_view(), name = 'add'),
    path('<slug:slug>/', detail , name= 'detail'),
    path('search', search, name= 'search'),
    path('cat', categories , name= 'categories'),
    path('category', category , name= 'category'),
    path('category/<slug:slug>',category_post , name= 'category'),
    path('tag/<slug:slug>/', tagged, name="tagged"),
]