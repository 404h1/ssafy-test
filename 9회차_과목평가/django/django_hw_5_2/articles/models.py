from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    update_at = models.DateTimeField( auto_now_add=True)

    