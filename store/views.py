import socket

from django.shortcuts import render

from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.


def Stalls(request):
    articles = Article.objects.filter(verified=True).order_by('-id')[:4]
    return render(request, 'store/home.html', {"articles": articles})


def single_post(request, article_name):
    print(article_name)
    article_obj = Article.objects.get(link_identifier=article_name)
    content = Content.objects.filter(article=article_obj).order_by('id')
    subtitle = Article.objects.filter(link_identifier=article_name).values_list('sub_title', flat=True).last()
    date = Article.objects.filter(link_identifier=article_name).values_list('date_added', flat=True).last()

    title = Article.objects.filter(link_identifier=article_name).values_list('title', flat=True).last()

    name = Article.objects.filter(link_identifier=article_name).values_list('author', flat=True).last()
    real_name_hehe = Author.objects.filter(pk=name).values_list('name', flat=True).last()
    background_image = Article.objects.filter(link_identifier=article_name).values_list('background_image',
                                                                                        flat=True).last()

    cat_pk = Article.objects.filter(link_identifier=article_name).values_list('category', flat=True).last()
    cat = Categories.objects.filter(pk=cat_pk).values_list('category', flat=True).last()

    # similar_articles = Article.objects.filter.exclude(link_identifier='article_name')(category=cat_pk).
    similar_articles = Article.objects.filter(~Q(link_identifier=article_name), category=cat_pk)[:4]
    print(similar_articles)

    times_clicked = Article.objects.filter(link_identifier=article_name).values_list('times_clicked', flat=True).last()
    times_clicked = times_clicked + 1

    art = Article.objects.get(link_identifier=article_name)
    art.times_clicked = times_clicked
    art.save()

    print('cat ', cat)

    print(subtitle)
    # print('name', background_image)
    context = {'content': content,
               'article_name': title,
               'subtitle': subtitle,
               'date': date,
               'name': real_name_hehe,
               'background_image': background_image,
               'category': cat,
               'similar_articles': similar_articles,
               'category_pk': cat_pk

               }
    return render(request, 'store/post.html', context)


def About(request):
    return render(request, 'store/about.html')


def Contact(request):
    return render(request, 'store/contact.html')


def load_more_posts(request):
    fruit = request.GET.get('type', 'aijawork bro')
    print('--->', fruit)
    if fruit == 'all':
        articles_list = Article.objects.order_by('-id')
    else:
        category_obj = Categories.objects.get(category=fruit)
        articles_list = Article.objects.filter(category=category_obj).order_by('-id')

    page = request.GET.get('page', 1)

    paginator = Paginator(articles_list, 4)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'store/more_posts.html', {"articles": articles, "fruit": fruit})


def privacy_policy(request):
    privacy = PrivacyPolicy.objects.all()
    return render(request, 'store/PrivacyPolicy.html', {"privacy": privacy})


def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        articles_list = Article.objects.filter(title__icontains=search_term)
        print(search_term)
        page = request.GET.get('page', 1)

        paginator = Paginator(articles_list, 4)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

    return render(request, 'store/more_posts.html', {"articles": articles})
