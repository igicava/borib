from django.shortcuts import render
from django.http import HttpResponse
from main.models import News

def index(request):
    context = {
        "posts": News.objects.all(),
    }
    return render(request, 'main/index.html', context)
