from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Article

# Create your views here..


def index(request):
    articles = Article.objects.all()
    content = {
        'articles': articles
    }
    for a in articles:
        print(a)
    return render(request, 'articles.html', content)


def article(request, id):
    art = Article.objects.get(id=int(id))
    content = {
        'article' : art
    }
    return render(request, 'single.html', content)
    pass