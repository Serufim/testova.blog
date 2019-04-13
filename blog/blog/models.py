from django.db import models

# Create your models here.
class BlogPost(models):
    title = models.CharField(max_length=255)
    text = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models):
    email = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    visible = models.BooleanField(default=True)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.email} - {self.text}"
