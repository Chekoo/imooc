#coding=utf-8
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __unicode__(self):   #返回标题，否则将返回ArticleObject
        return self.title