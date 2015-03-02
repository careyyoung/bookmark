# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'bookmark/hello_project.html')
