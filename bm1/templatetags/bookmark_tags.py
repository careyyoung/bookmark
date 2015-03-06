# -*- coding: UTF-8 -*-
'''
Created on 2015年3月3日

@author: carey.yang
'''
from django import template 
register = template.Library() 

#用于前台显示截断过长字符串
@register.filter("truncate_chars")
def truncate_chars(value, max_length):
        if len(value) > max_length:
                truncd_val = value[:max_length]
                if not len(value) == max_length+1 and value[max_length+1] != " ":
                        truncd_val = truncd_val[:truncd_val.rfind(" ")]
                return  truncd_val + "..."
        return value
