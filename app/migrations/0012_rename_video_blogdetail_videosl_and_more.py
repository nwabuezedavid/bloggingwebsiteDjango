# Generated by Django 4.0.6 on 2022-12-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_blogdetail_category_alter_blogdetail_imgae'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetail',
            old_name='video',
            new_name='videoSl',
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('lovedvideo', 'lovedvideo'), ('facebook', 'facebook'), ('music', 'music'), ('comedy', 'comedy'), ('websitesale', 'websitesale'), ('hacked app', 'hackedapk'), ('insparitional', 'insparitional'), ('news', 'news'), ('jobs', 'jobs'), ('twitter', 'twitter'), ('website', 'website'), ('fashion', 'fashion'), ('sport', 'sport'), ('entertainment', 'entertainment'), ('books', 'books'), ('movies', 'movies')], max_length=50, null=True),
        ),
    ]