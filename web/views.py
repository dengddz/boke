from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from backsys.models import Article, ArticleType


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'web/index.html', {'articles': articles})


def list(request, id=1):
    if request.method == 'GET':
        articles = Article.objects.filter(a_f=id)
        arttypes = ArticleType.objects.all()
        atype_now = ArticleType.objects.filter(pk=id).first().type
        page = int(request.GET.get('page', 1))
        paginator = Paginator(articles, 2)
        page = paginator.page(page)
        url = '/web/list/' + id + '/'
        return render(request, 'web/list.html', {'page': page, 'arttypes': arttypes, 'atype_now':atype_now, 'url':url})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


def info(request, id):
    if request.method == 'GET':
        # 需要改----------------------------
        article = Article.objects.filter(pk=id).first()
        arttypes = ArticleType.objects.all()
        atype_now = article.a_f.type
        return render(request, 'web/info.html', {'article': article, 'arttypes': arttypes, 'atype_now':atype_now})