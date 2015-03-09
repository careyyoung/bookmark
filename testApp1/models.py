# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

class time_stamped_model(models.Model):
    """
    abstract base class, 提供创建时间和修改时间两个通用的field
    """
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
#class test(time_stamped_model): #继承abstract base class:time_stamped_model,test表就有上面通用的field
#    test1 = models.CharField(max_length=200)

class test(time_stamped_model):
    username = models.CharField(max_length=20)

