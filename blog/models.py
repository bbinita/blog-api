from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    NAME_CHOICES = [
        ('LIFESTYLE', 'lifestyle'),
        ('FASHION', 'fashion'),
        ('FOOD', 'food'),
        ('TRAVEL', 'travel'),
        ('TECHNOLOGY', 'technology'),
        ('PERSONALFINANCE', 'personal-finance'),
        ('HEALTH/FITNESS', 'health/fitness'),
        ('MARKETING', 'marketing'),
        ('DIY', 'diy'),
    ]

    name = models.CharField(
        max_length=20,
        choices = NAME_CHOICES,
        default='TECHNOLOGY'
    )



class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name = 'posts'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )