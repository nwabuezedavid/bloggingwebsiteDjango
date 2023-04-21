from django.db import models

# Create your models here.




    

    
CHOICES_CATEGORY = {
    ('facebook', 'facebook'),
    ('twitter', 'twitter'),
    ('entertainment', 'entertainment'),
    ('sport', 'sport'),
    ('movies', 'movies'),
    ('comedy', 'comedy'),
    ('insparitional', 'insparitional'),
    ('websitesale', 'websitesale'),
    ('website', 'website'),
    ('music', 'music'),
    ('jobs', 'jobs'),
    ('hacked app', 'hackedapk'),
    ('lovedvideo', 'lovedvideo'),
    ('news', 'news'),
    ('fashion', 'fashion'),
    ('books', 'books'),

}        
class blogDetail(models.Model):
    title = models.CharField(max_length=3000, blank=True, null=True)
    dateCreated = models.DateField(auto_now_add=True)
    like = models.IntegerField(blank=True, null=True , default=233)
    text = models.TextField(blank=True, null=True)
    videoSl = models.FileField(  max_length=100000, blank=True, null=True)
    imgae = models.ImageField(  max_length=100000, blank=True, null=True)
    category = models.CharField(choices=CHOICES_CATEGORY,max_length=50, blank=True, null=True)
    facebook = models.URLField(max_length=500000,blank=True, null=True)
    whatsapp = models.URLField(max_length=500000,blank=True, null=True)
    twitter = models.URLField(max_length=500000,blank=True, null=True)
    youtube = models.URLField(max_length=500000,blank=True, null=True)
    instragram = models.URLField(max_length=500000,blank=True, null=True)
    
    

    def __str__(self):
        return str(self.title) + "     FAMILY OF  " + str(self.category )

