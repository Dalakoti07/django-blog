from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'author':"Narsimha",
        "title":"Data structure",
        "content":"some",
        "date posted":"yesterday"
    },
        {
        'author':"Narsimha 2",
        "title":"Data structure 2",
        "content":"some 2",
        "date posted":"Today"
    }
]


def home(request):
    context={
        'posts_key':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':"Title"})