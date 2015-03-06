# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.


class TimeStampedModel(models.Model):
    """
    abstract base class, 提供创建时间和修改时间两个通用的field
    """
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True










class bookmarks1(models.Model):
    parent = models.IntegerField(null=True)
    bid = models.IntegerField()
    fk = models.IntegerField()
    title = models.CharField(max_length=250,blank=True)
    position = models.IntegerField()
    url = models.URLField(max_length=250,blank=True)
    description = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.title 

class citys1(models.Model):
    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'
    city_name = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.city_name


class sale_orders1(models.Model):
    class Meta:
        verbose_name = '销售订单'
        verbose_name_plural = '销售订单' 
    
    month_choices = (
                    ('January',u'一月'),
                    ('February',u'二月'),
                    ('March',u'三月'),
                    ('April',u'四月'),
                    ('May',u'五月'),
                    ('June',u'六月'),
                    ('July',u'七月'),
                    ('August',u'八月'),
                    ('September',u'九月'),
                    ('October',u'十月'),
                    ('November',u'十一月'),
                    ('December',u'十二月'),
                    )
    
    city = models.ForeignKey(citys1,  related_name= 'cityID', verbose_name='城市')  
    month = models.CharField(max_length=250,choices=month_choices,default="")
    value = models.IntegerField()
    
    def __unicode__(self):
        return u"%s %s %s" % (self.month,self.city,self.value)

class Note(models.Model):
    title = models.CharField(max_length=250,verbose_name='标题',default="")  
    content = models.CharField(max_length=250,verbose_name='内容',default="") 
    create_time = models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = '笔记'
        ordering = ('-create_time',)
    
    def __unicode__(self):
        return "%s~~~~%s" % (self.title, self.create_time)





