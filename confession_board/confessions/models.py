from django.db import models

# Create your models here.
# confessions/models.py

# confessions/models.py

from django.db import models

class Confession(models.Model):
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

class Comment(models.Model):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
