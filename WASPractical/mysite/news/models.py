import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    headline = models.CharField(max_length=200)
    published = models.DateTimeField('date published')
    sub_heading = models.CharField(max_length=1000)

    def __str__(self):
        return self.headline

    def pub_date(self):
        return self.published

    def __str__(self):
        return self.sub_heading
