# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from bm1.serializers import NoteViewSet
#from bookmark.settings import dev


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)


    
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'bookmark.views.hello',),
    url(r'^bm1/hello/$', 'bm1.views.hello',),
    url(r'^bm1/bookmarks/$', 'bm1.views.bookmarks',),
    url(r'^bm1/dashboard/$', 'bm1.views.dashboard',),
    url(r'^bm1/chart_demo/$', 'bm1.views.chart_demo',),
    url(r'^bm1/note_demo/$', 'bm1.views.note_demo',),
    
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    
    
    url(r'^testApp1/hello/$', 'testApp1.views.hello',),
    url(r'^testApp1/login/$', 'testApp1.views.login',),
    url(r'^testApp1/listmsg/$', 'testApp1.views.listmsg',),
    url(r'^testApp1/testform/$', 'testApp1.views.testform',),
    url(r'^testApp1/search/', 'testApp1.views.search',),

    
)


#if dev.DEBUG:
#    urlpatterns += patterns('', 
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': dev.MEDIA_ROOT }),
#    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': dev.STATIC_ROOT}),
#)
