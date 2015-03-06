# -*- coding: UTF-8 -*-
'''
Created on 2015年3月5日

@author: carey.yang
'''
from models import Note
from pagedown.widgets import AdminPagedownWidget
from django import forms

class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Note
