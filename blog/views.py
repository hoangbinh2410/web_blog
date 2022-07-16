from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from . models import Post
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
class HomeView(ListView):
    model = Post
    template_name = "home.html"

class DetailView(DetailView):
    model = Post
    template_name = "detail_blog.html"
class AddBlogView(CreateView):
     model = Post
     template_name = 'addblock.html'
     fields = '__all__'