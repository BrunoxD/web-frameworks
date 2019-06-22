from datetime import date
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter

# Create your models here.
class BlogAuthor(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    bio = models.TextField(max_length=500, help_text='Enter your bio details here.')

    class Meta:
        ordering = ["name", "bio"]

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.name.username

class Blog(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=5000, help_text="Enter you blog text here.")
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    description = models.TextField(max_length=2000, help_text="Enter comment about blog here.")
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring


