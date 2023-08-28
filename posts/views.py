from django.shortcuts import render

# Third party imports
from . models import Post

# Create your views here.
def blog_page(request):
    posts = Post.objects.all()
    return render(request, 'posts/blog.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts/post.html', {'posts': posts})