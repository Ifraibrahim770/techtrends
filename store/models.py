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

    def __str__(self):
        return str(self.title)


class Content(models.Model):
    title1 = models.TextField(max_length=2000, null=True)
    para1_1 = models.TextField(max_length=2000, null=True)
    para1_2 = models.TextField(max_length=2000, null=True)
    para1_3 = models.TextField(max_length=2000, null=True)
    para1_4 = models.TextField(max_length=2000, null=True)
    image1 = models.ImageField(blank=True, null=True)

    title2 = models.TextField(max_length=2000, null=True)
    para2_1 = models.TextField(max_length=2000, null=True)
    para2_2 = models.TextField(max_length=2000, null=True)
    para2_3 = models.TextField(max_length=2000, null=True)
    para2_4 = models.TextField(max_length=2000, null=True)
    image2 = models.ImageField(blank=True, null=True)

    title3 = models.TextField(max_length=2000, null=True)
    para3_1 = models.TextField(max_length=2000, null=True)
    para3_2 = models.TextField(max_length=2000, null=True)
    para3_3 = models.TextField(max_length=2000, null=True)
    para3_4 = models.TextField(max_length=2000, null=True)
    image3 = models.ImageField(blank=True, null=True)

    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.article)

    @property
    def imageURL(self):
        try:
            url = self.image1.url

        except:
            url = ''
        return url

    def image2URL(self):
        try:
            url = self.image2.url

        except:
            url = ''
        return url

    def image3URL(self):
        try:
            url = self.image3.url

        except:
            url = ''
        return url
