# -*- coding: UTF-8 -*-
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse
from testApp1.forms import LoginForm
# Create your views here.

# hello just for testing. 
#1. goto common.py, "'testApp1'," appended to INSTALLED_APPS next line 33.
#2. goto hello_app.html, change line 3 to the correct name
#3. goto urls.py, change line 12 to the correct name
#4. access http://127.0.0.1:9999/testApp1/hello
def hello(request):
    return render(request, 'testApp1/hello_app.html')

# Create your views here.

def login(request):

    a = 'username' in request.POST
    if a:
        username = request.POST['username']
        form = LoginForm({'username':username})
        test = form.save(commit=False)
        test.save()
        form.save()
        print 'hahah'
        return render_to_response('testApp1/login.html',RequestContext(request,{'username':username}))
    else:
        username = ''
        print '555'
        return render_to_response('testApp1/login.html',RequestContext(request,{'username':username}))
    
    
def listmsg(request):
    request_get_host = request.get_host()
    request_path = request.path
    request_get_full_path = request.get_full_path()
    
    request_method = request.META.get('REQUEST_METHOD', 'unknown')
    content_type = request.META.get('CONTENT_TYPE', 'unknown')
    user_agents = request.META.get('HTTP_USER_AGENT', 'unknown')
    http_cookie = request.META.get('HTTP_COOKIE', 'unknown')
    http_host = request.META.get('HTTP_HOST', 'unknown')
    http_referer = request.META.get('HTTP_REFERER', 'unknown')
    processor_arch = request.META.get('PROCESSOR_ARCHITECTURE', 'unknown')
    processor_identifier = request.META.get('PROCESSOR_IDENTIFIER', 'unknown')
    remote_addr = request.META.get('REMOTE_ADDR', 'unknown')
    dict1 = {
            'request_get_host' : request_get_host,
            'request_path' : request_path,
            'request_get_full_path' : request_get_full_path,
            'request_method' : request_method,
            'content_type' : content_type,
            
            'user_agents' : user_agents,
            'http_cookie' : http_cookie,
            'http_host' : http_host,
            'http_referer' : http_referer,
            'processor_arch' : processor_arch,
            
            'processor_identifier' : processor_identifier,
            'remote_addr' :remote_addr,
            }
    
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
        
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))

    
    return render_to_response('testApp1/listmsg.html',RequestContext(request,{"dict1":dict1}))




def testform(request):
    return render_to_response('testApp1/form.html')

def search(request):
    query = request.GET.get('q','')
    if query:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
