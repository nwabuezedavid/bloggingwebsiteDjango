# Generated by Django 4.0.6 on 2022-12-10 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_video_blogdetail_videosl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('books', 'books'), ('fashion', 'fashion'), ('comedy', 'comedy'), ('website', 'website'), ('facebook', 'facebook'), ('music', 'music'), ('lovedvideo', 'lovedvideo'), ('insparitional', 'insparitional'), ('news', 'news'), ('entertainment', 'entertainment'), ('hacked app', 'hackedapk'), ('twitter', 'twitter'), ('movies', 'movies'), ('jobs', 'jobs'), ('websitesale', 'websitesale'), ('sport', 'sport')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='imgae',
            field=models.ImageField(blank=True, max_length=100000, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='videoSl',
            field=models.FileField(blank=True, max_length=100000, null=True, upload_to=''),
        ),
    ]