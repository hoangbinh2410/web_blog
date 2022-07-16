
from django.urls import path
from .views import UserLoginView
urlpatterns = [
path('register', UserLoginView.as_view(),name='register')
]