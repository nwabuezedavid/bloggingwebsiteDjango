# Generated by Django 4.0.6 on 2022-12-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_blogdetail_poster_alter_blogdetail_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetail',
            name='file',
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='imgae',
            field=models.FileField(blank=True, max_length=100000, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='video',
            field=models.FileField(blank=True, max_length=100000, null=True, upload_to='video'),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('news', 'news'), ('sport', 'sport'), ('jobs', 'jobs'), ('insparitional', 'insparitional'), ('movies', 'movies'), ('website', 'website'), ('comedy', 'comedy'), ('facebook', 'facebook'), ('lovedvideo', 'lovedvideo'), ('fashion', 'fashion'), ('books', 'books'), ('websitesale', 'websitesale'), ('music', 'music'), ('entertainment', 'entertainment'), ('twitter', 'twitter'), ('hacked app', 'hackedapk')], max_length=50, null=True),
        ),
    ]