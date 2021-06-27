from django.shortcuts import render,get_object_or_404
from .models import Article


def all_articles(request):
    all_articles = Article.objects.filter(status='publish')
    return render(request, 'blog/all_articles.html', {'all_articles': all_articles})


def article_detail(request, id):
    article_detail = Article.objects.get(id=id)
    return render(request, 'blog/article_detail.html', {'article_detail': article_detail})
