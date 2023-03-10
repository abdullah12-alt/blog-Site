from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text= models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_data= models.DateTimeField(blank=True,null=True) 