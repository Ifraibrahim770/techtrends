# Generated by Django 3.1.1 on 2021-06-17 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_identifier', models.CharField(max_length=2000, null=True)),
                ('title', models.CharField(max_length=2000, null=True)),
                ('sub_title', models.CharField(max_length=2000, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('times_clicked', models.IntegerField(default=0)),
                ('verified', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MobileVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=2000, null=True)),
                ('verification_code', models.CharField(max_length=2000, null=True)),
                ('count', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoneNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=2000, null=True)),
                ('verified', models.BooleanField(default=False, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(blank=True, default=0, null=True)),
                ('review', models.CharField(max_length=2000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productcategory'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.TextField(max_length=2000, null=True)),
                ('para1_1', models.TextField(max_length=2000, null=True)),
                ('para1_2', models.TextField(max_length=2000, null=True)),
                ('para1_3', models.TextField(max_length=2000, null=True)),
                ('para1_4', models.TextField(max_length=2000, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('title2', models.TextField(max_length=2000, null=True)),
                ('para2_1', models.TextField(max_length=2000, null=True)),
                ('para2_2', models.TextField(max_length=2000, null=True)),
                ('para2_3', models.TextField(max_length=2000, null=True)),
                ('para2_4', models.TextField(max_length=2000, null=True)),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('title3', models.TextField(max_length=2000, null=True)),
                ('para3_1', models.TextField(max_length=2000, null=True)),
                ('para3_2', models.TextField(max_length=2000, null=True)),
                ('para3_3', models.TextField(max_length=2000, null=True)),
                ('para3_4', models.TextField(max_length=2000, null=True)),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.categories'),
        ),
    ]
