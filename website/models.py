from django.db import models
from django.contrib.auth.models import User

# Create your models here.
index = [
    ("index","index"),
    ("noindex","noindex")]
    
follow = [
    ("follow","follow"),
    ("nofollow","nofollow")]  

types = [
    ('Residential','Residential'),
    ('2','Commercial'),
]
furnish = [
    ("1","Semi-Furnish"),
    ("2","Fully-Furnish"),
]
status = [
    ('1','Draft'),
    ('2','Available'),
    ('3','Sold'),
]

class agent (models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to="./",default="NA")
    
    def __str__(self):
        return self.name

    
class property(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    room = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length = 1000, default="Text")
    address = models.CharField(max_length=200)
    type = models.CharField(choices=types, default='1',max_length=12)
    furnis = models.CharField(choices=furnish, default='1',max_length=1)
    stat = models.CharField(choices=status, default='2',max_length=1)
    agent = models.ForeignKey(agent, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    image1 =models.ImageField(upload_to="./property/")
    
    def __str__(self):
        return self.name
    
class blog(models.Model):
    choice = [
        ('1',"Draft"),
        ('2',"Published"),
    ]
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="./blog/",blank=True)
    altTag = models.CharField(max_length=100,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.TextField(blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(max_length = 50)
    banner = models.ImageField(upload_to='./blog/')
    altTag1 = models.CharField(max_length=100,blank=False)
    page_title = models.CharField(max_length=200)
    meta = models.CharField(max_length=400)
    STATUS = models.CharField(max_length=2, choices=choice, default=1)
    index = models.CharField(max_length=8, choices=index, default="index")
    follow = models.CharField(max_length=8, choices=follow, default="follow")
    
    def __str__(self):
        return self.title

class images(models.Model):
    listing  = models.ForeignKey(property, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="./property/",blank=True)