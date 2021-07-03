# Generated by Django 3.1.1 on 2021-06-23 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarouselImages',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='MobileVerification',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productdescription',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
        migrations.RemoveField(
            model_name='userphonenumbers',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductDescription',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
        migrations.DeleteModel(
            name='UserPhoneNumbers',
        ),
    ]