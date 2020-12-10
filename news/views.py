from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import News
from .forms import FeedbackForm


def index(request):
    news = News.objects.all()

    return render(request, 'index.html', {'news': news})


def news_item(request, tr):
    try:
        news = News.objects.get(tr=tr)
    except News.DoesNotExist:
        raise Http404
    return render(request, 'news/news.html', {'news': news})


def feedback_new(request):
    if request.method == "POST":
        feedback = FeedbackForm(request.POST, request.FILES)
        if feedback.is_valid():
            feedback.save()
    else:
        feedback = FeedbackForm()

    return render(request, 'feedback.html', {'feedback': feedback})
