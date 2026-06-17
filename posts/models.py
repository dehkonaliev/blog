from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=600)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
    