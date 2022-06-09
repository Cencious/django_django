from poplib import POP3_SSL_PORT
from django.shortcuts import render


posts =  [
    {
        'authors':'Inno',
        'title':'Insta Post',
        'content':'First post content',
        'date_posted':'August 27,2021'

    },
    {
        'authors':'Jane',
        'title':'Insta Post 2',
        'content':'Second post content',
        'date_posted':'August 29,2021'

    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'insta/home.html', context)

def about(request):
 return render(request,'insta/about.html')