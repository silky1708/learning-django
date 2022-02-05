from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    allPosts = Post.objects.all()
    return render(request, 'index.html', {'allPosts': allPosts})