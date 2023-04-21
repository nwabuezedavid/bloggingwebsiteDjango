# Generated by Django 4.0.6 on 2022-12-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_blogdetail_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('sport', 'sport'), ('twitter', 'twitter'), ('news', 'news'), ('jobs', 'jobs'), ('comedy', 'comedy'), ('insparitional', 'insparitional'), ('books', 'books'), ('websitesale', 'websitesale'), ('entertainment', 'entertainment'), ('fashion', 'fashion'), ('website', 'website'), ('movies', 'movies'), ('lovedvideo', 'lovedvideo'), ('music', 'music'), ('facebook', 'facebook'), ('hacked app', 'hackedapk')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='poster',
            field=models.ImageField(blank=True, max_length=10000, null=True, upload_to='blogPoster'),
        ),
    ]
