from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def home(request):
    return render(request, 'posts/home.html')

def blog_page(request):
    return render(request, 'posts/blog.html')
