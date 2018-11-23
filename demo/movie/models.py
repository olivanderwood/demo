from django.db import models

# Create your models here.
class Post1(models.Model):
    title = models.CharField(max_length=100)
    body =models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True, null=True, upload_to="poster")
    bgm =models.ImageField(blank=True, null=True, upload_to="backgroundmovie")
    time =models.TextField(default='')

    def __str__(self):
        return self.title