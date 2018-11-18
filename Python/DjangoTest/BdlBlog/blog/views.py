from django.shortcuts import render
# render方法用于渲染Html页面，
# 使用方法：直接return render
# from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    # return HttpResponse("My First Django Response！")
    article = models.Article.objects.get(pk=1)
    return render(request, "blog/index.html", {"h1_text": "Hello My Django Blog Web!",
                                               "article": article})

def main(request):
    articles = models.Article.objects.all()
    return render(request, "blog/main.html", {"articles": articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article.html", {"article": article})

def edit_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/edit_page.html", {"article": article})

def edit_action(request, article_id):
    title = request.POST.get("title", "标题")
    content = request.POST.get("content", "内容")
    # models.Article.objects.create(title=title, content=content)
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return article_page(request,article_id)