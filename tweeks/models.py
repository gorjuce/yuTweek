from django.db import models
from django.contrib.auth.models import User


class Tweek(models.Model):
    content = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='author')
    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.content