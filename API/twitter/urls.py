from django.urls import path

from . import views
from . import register
from . import login
from . import tweet

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet', tweet.tweet, name='tweet'),
    path('register', register.register, name='register'),
    path('login', login.login, name='login'),
]