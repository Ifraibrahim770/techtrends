from django.urls import path
from . import views

urlpatterns = [

    path('', views.Stalls, name="stalls"),
    path('post', views.single_post, name="single_post"),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    path('morePosts/', views.load_more_posts, name='morePosts'),
    path('privacy', views.privacy_policy, name='privacy'),
    path('search/', views.search, name='search'),
    path('search/post/<str:article_name>', views.single_post, name="single_post"),
    path('morePosts/post/<str:article_name>', views.single_post, name="single_post"),


]
