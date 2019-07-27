from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author':'sergioCG',
        'title':'Blog1',
        'content':'Primer post',
        'date':'Junio 27'
    },
    {
        'author':'sergioCG1',
        'title':'Blog2',
        'content':'Primer post 1',
        'date':'Junio 27'
    },
]

def home(request):
    context = {
        'post': post
    }
    return render(request,'blog/home.html',context)

def about(request):
     return render(request,'blog/about.html',{'title':'about'})

