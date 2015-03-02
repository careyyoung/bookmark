# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.

# hello just for testing. 
#1. goto common.py, "'bm1'," appended to INSTALLED_APPS next line 33.
#2. goto hello_app.html, change line 3 to the correct name
#3. goto urls.py, change line 12 to the correct name
#4. access http://127.0.0.1:9999/bm1/hello
def hello(request):
    return render(request, 'bm1/hello_app.html')

# Create your views here.
