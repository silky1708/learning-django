from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    allPosts = Post.objects.all()
    return render(request, 'index.html', {'allPosts': allPosts})

def posts(request, page_id):
    post = Post.objects.get(id=page_id)
    return render(request, 'posts.html', {'post':post})