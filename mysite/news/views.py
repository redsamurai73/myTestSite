from django.shortcuts import render
from .models import News
from .translit import prepare_url


def main_news(request):
    news = News.objects.all()

    news_translit = [prepare_url(i) for i in news]
    return render(request, 'news/main.html', {'news': news, 'news_translit': news_translit})
