from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from myproject.myapp3.models import Author, Article, Comment
# Create your views here.


def hello(request):
    return HttpResponse("<h1>Hello World from Function!</h1>")


class HelloView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World from Class!</h1>")


def year_post(request, year):
    text = ""
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii':False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context



def get_articles(request, author_id: int):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author.id)
    context = {
        'articles': articles
    }
    return render(request, 'myapp/new.html', context=context)


def detail_article(request, article_id: int):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('-change_at')
    article.count_views += 1
    article.save()
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'myapp/detail.html', context=context)
