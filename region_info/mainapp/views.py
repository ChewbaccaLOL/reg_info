from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ChewbaccaLOL',
        'title': 'Article Post 1',
        'content':'First article',
        'date_posted': '02.05.2020'
    },
    {
        'author': 'admin001',
        'title': 'Article Post 2',
        'content':'Second article',
        'date_posted': '03.05.2020'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'infoservice/home.html', context)

def about(request):
    return render(request, 'infoservice/about.html', {'title':'About'})


