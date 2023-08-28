from django.shortcuts import render

# Third party imports
from . models import Post

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def home(request):
    return render(request, 'posts/home.html')

def blog_page(request):
    posts = Post.objects.all()
    return render(request, 'posts/blog.html', {'posts': posts})
