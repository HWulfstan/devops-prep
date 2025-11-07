

from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=280)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

