from django.urls import path
from . import views

urlpatterns = [

    path('', views.Stalls, name="stalls"),
    path('post/<str:article_name>', views.single_post, name="single_post"),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    path('morePosts', views.load_more_posts, name='morePosts'),

]
