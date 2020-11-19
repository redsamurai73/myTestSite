from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()

    return render(request, 'index.html', {'news': news})


def news_item(request, tr):
    news = News.objects.get(tr=tr)

    return render(request, 'news/news.html', {'news': news})
