# -*- coding: UTF-8 -*-
'''
Created on 2015年3月9日

@author: carey.yang
'''
from django import forms
from testApp1.models import test

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=20)

    class Meta:
        model = test