# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from bm1.models import bookmarks1,sale_orders1,citys1,Note,ContactForm

# Create your views here.

# hello just for testing. 
#1. goto common.py, "'bm1'," appended to INSTALLED_APPS next line 33.
#2. goto hello_app.html, change line 3 to the correct name
#3. goto urls.py, change line 12 to the correct name
#4. access http://127.0.0.1:9999/bm1/hello
def hello(request):
    return render(request, 'bm1/hello_app.html')

# Create your views here.
def bookmarks(request):
    bm_list = bookmarks1.objects.exclude(url='')
    bm_list1 = bookmarks1.objects.exclude(url='')[0:50]
    bm_list2 = bookmarks1.objects.all()[50:100]
    bm_list3 = bookmarks1.objects.all()[100:150]
    bm_list4 = bookmarks1.objects.all()[150:200]
    
    print bm_list1
    
    #return render(request, 'bm1/bookmarks.html' ,{'bm_list':bm_list})
    return render_to_response('bm1/bookmarks.html', 
                              {
                                'bm_list1':bm_list1,
                                'bm_list2':bm_list2,
                                'bm_list3':bm_list3,
                                'bm_list4':bm_list4,
                              },
                              context_instance=RequestContext(request)
    )
    
def dashboard(request):
    return render(request, 'bm1/dashboard.html')

def chart_demo(request):
    data1 = sale_orders1.objects.filter(city_id=1)
    labels1 = []
    for x in data1:
        labels1.append(str(x.month))
    
    
    datas1 = []
    for x in data1:
        datas1.append(int(x.value))
    
        
    fillColor1 = "rgba(151,187,205,0.5)"
    strokeColor1 = "rgba(151,187,205,1)"
    pointColor1 = "rgba(151,187,205,1)"
    pointStrokeColor1 = "#fff"
    
    disct1 = {
              'fillColor':fillColor1, 
              'strokeColor':strokeColor1, 
              'pointColor':pointColor1, 
              'pointStrokeColor':pointStrokeColor1, 
              'data':datas1
              }
    data_list = [disct1]
    return render(request, 
                  'bm1/chart_demo.html',
                  {'labels':labels1,'data_list':data_list}
                  )

def note_demo(request):
    note = Note.objects.get(id=4)
    return render(request, 'bm1/note_demo.html',{"note":note})
