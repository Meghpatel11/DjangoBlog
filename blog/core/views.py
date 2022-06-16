from django.shortcuts import render

from postsk.models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request,'core/home.html',{'posts':posts})

def about(request):
    return render(request,'core/about.html')
    