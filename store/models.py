from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return str(self.name)


class Categories(models.Model):
    category = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return str(self.category)


class Article(models.Model):
    link_identifier = models.CharField(max_length=2000, null=True)
    title = models.CharField(max_length=2000, null=True)
    sub_title = models.CharField(max_length=2000, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    times_clicked = models.IntegerField(default=0)
    verified = models.BooleanField(default=False, blank=False, null=True)
    background_image = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    @property
    def imageURL(self):
        try:
            url = self.background_image.url

        except:
            url = ''
        return url


class Content(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    paragraph = models.TextField(max_length=2000, null=True, blank=True)
    image1 = models.CharField(max_length=2000, blank=True, null=True)
    image_caption = models.CharField(max_length=2000, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    list_items = models.TextField(max_length=2000, null=True, blank=True)
    youtube = models.CharField(max_length=2000, null=True,blank=True)

    def __str__(self):
        return str(self.article)


class AboutMe(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    paragraph = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.paragraph[0:15])



