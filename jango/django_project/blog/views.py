from django.shortcuts import render
from django.http import HttpResponse,Http404
from.models import Post
from django.template import loader
from .models import Post

posts=[
    {
        'author':'pradeep',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'june 12, 2020'
    },
    {
        'author':'Hasini',
        'title':'Blog Post 2',
        'content':'second post content',
        'date_posted':'june 12, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/index.html', context)

def about(request):
    return render(request,'blog/detail.html',{'title':'About'})




