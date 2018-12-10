from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.urls import reverse
# Create your views here.
from django.urls import reverse

from backsys.Artform import AddArtForm
from backsys.models import SuperUser, Article, ArticleType


# Create your views here.



def login(request):
    if request.method == 'GET':
        return render(request, 'backsys/login.html')
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = SuperUser.objects.filter(username=user, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return HttpResponseRedirect('/backsys/index/')
        else:
            err = '账号密码有误，请重新输入'
            return render(request, 'backsys/login.html', {'error': err})



def index(request):
    if request.method == 'GET':
        return render(request, 'backsys/index.html')


def article(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        arttypes = ArticleType.objects.all()
        page = int(request.GET.get('page', 1))
        paginator = Paginator(articles, 2)
        page = paginator.page(page)
        return render(request, 'backsys/article.html', {'arttypes': arttypes, 'page': page})


def add_article(request):
    if request.method == 'GET':
        arttypes = ArticleType.objects.all()
        return render(request, 'backsys/add-article.html',{'arttypes': arttypes})
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        # form.is_valid，验证参数是否有效，如验证成功，返回True，反之False
        if form.is_valid():
            a_title = form.cleaned_data['a_title']
            a_content = form.cleaned_data['a_content']
            a_keywords = form.cleaned_data['a_keywords']
            a_describe = form.cleaned_data['a_describe']
            a_titlepic = form.cleaned_data['a_titlepic']
            # a_f , TypeError: int() argument must be a string, a bytes-like object or a number, not 'builtin_function_or_method'
            a_f = request.POST.get('a_f')
            a_f_form = ArticleType.objects.filter(pk=a_f).first()
            # 判断a_f是否存在
            if not a_f_form:
                form = '所选类型不存在'
                return render(request, 'backsys/add-article.html', {'err': form})
            art = Article()
            art.a_describe = a_describe
            art.a_content = a_content
            art.a_keywords = a_keywords
            art.a_title = a_title
            art.a_titlepic = a_titlepic
            art.a_f = a_f_form
            art.save()
            return HttpResponseRedirect(reverse('backsys:article'))
        else:
            # 验证失败
            arttypes = ArticleType.objects.all()
            return render(request, 'backsys/add-article.html', {'err': form, 'arttypes': arttypes})


def del_art(request, id):
    if request.method == 'GET':
        # 查询文章 并 删除
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backsys:article'))


def edit_art(request, id):
    if request.method == 'GET':
        # 查询文章
        article = Article.objects.filter(pk=id).first()
        arttypes = ArticleType.objects.all()
        return render(request, 'backsys/add-article.html', {'article':article, 'arttypes': arttypes})

    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        # form.is_valid，验证参数是否有效，如验证成功，返回True，反之False
        if form.is_valid():
            a_title = form.cleaned_data['a_title']
            a_content = form.cleaned_data['a_content']
            a_keywords = form.cleaned_data['a_keywords']
            a_describe = form.cleaned_data['a_describe']
            a_titlepic = form.cleaned_data['a_titlepic']
            # a_f , TypeError: int() argument must be a string, a bytes-like object or a number, not 'builtin_function_or_method'
            a_f = request.POST.get('a_f')
            a_f_form = ArticleType.objects.filter(pk=a_f).first()
            # 判断a_f是否存在
            if not a_f_form:
                form = '所选类型不存在'
                return render(request, 'backsys/add-article.html', {'err': form})
            art = Article()
            art.a_describe = a_describe
            art.a_content = a_content
            art.a_keywords = a_keywords
            art.a_title = a_title
            art.a_titlepic = a_titlepic
            art.a_f = a_f_form
            art.save()
            return HttpResponseRedirect(reverse('backsys:article'))
        else:
            # 验证失败
            arttypes = ArticleType.objects.all()
            return render(request, 'backsys/add-article.html', {'err': form, 'arttypes': arttypes})