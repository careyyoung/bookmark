# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.


class bookmarks1(models.Model):
    parent = models.IntegerField(null=True)
    bid = models.IntegerField()
    fk = models.IntegerField()
    title = models.CharField(max_length=250)
    position = models.IntegerField()
    url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.title
