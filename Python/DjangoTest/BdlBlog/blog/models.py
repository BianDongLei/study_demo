from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=1000,default="标题")
    author = models.CharField(max_length=10,default="作者")
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
