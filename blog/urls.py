
from django.urls import path
from . import views
from .views import HomeView, DetailView,AddBlogView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="detail-blog"),
    path('newblock/', AddBlogView.as_view(), name='add-block'),
]