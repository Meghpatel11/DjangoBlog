from django.shortcuts import get_object_or_404, redirect, render

from .models import Post,Catogry
from .form import CommentForms

# Create your views here.

def details(request,category_slug,slug):
    post = get_object_or_404(Post,slug=slug)

    if request.method == 'POST':
        form = CommentForms(request.POST)

        if form.is_valid():
            # just save comment to variable
            comment = form.save(commit=False)
            # assign a comment to respective post
            comment.post = post
            # then save to database
            comment.save()

            # redirect to that post again by view
            return redirect('post_details',slug=slug)
            
    else:
        form = CommentForms()

    return render(request,'postsk/x.html', {'post':post, 'form':form})

def category(request,slug):
    category = get_object_or_404(Catogry,slug=slug)

    return render(request,'postsk/category.html',{'category':category})