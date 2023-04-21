# Generated by Django 4.0.6 on 2022-12-01 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_blogdetail_category_alter_blogdetail_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetail',
            name='like',
            field=models.IntegerField(blank=True, default=233, null=True),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('twitter', 'twitter'), ('lovedvideo', 'lovedvideo'), ('websitesale', 'websitesale'), ('website', 'website'), ('insparitional', 'insparitional'), ('books', 'books'), ('entertainment', 'entertainment'), ('fashion', 'fashion'), ('jobs', 'jobs'), ('music', 'music'), ('sport', 'sport'), ('news', 'news'), ('movies', 'movies'), ('hacked app', 'hackedapk'), ('comedy', 'comedy'), ('facebook', 'facebook')], max_length=50, null=True),
        ),
    ]