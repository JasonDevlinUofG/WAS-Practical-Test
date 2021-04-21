from django.shortcuts import render

from .models import Article


def articles(request):
    article_list = Article.objects.order_by('-published')[:5]
    context = {'article_list': article_list}
    return render(request, 'news/displayArticles.html', context)
