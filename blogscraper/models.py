from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    text = models.TextField()

    def __str__(self):
        return self.title
