from django.shortcuts import render
from .models import News


def main(request):
    news = News.objects.filter(published_date__lte=ti)
    return render(request, 'news/main.html', {})
